#ifndef SJTU_PRIORITY_QUEUE_HPP
#define SJTU_PRIORITY_QUEUE_HPP

#include <cstddef>
#include <functional>
#include "exceptions.hpp"

namespace sjtu {

template<typename T, class Compare = std::less<T>>
class priority_queue {
private:
    struct Node {
        T value;
        Node* left;
        Node* right;
        size_t dist;
        Node(const T& v) : value(v), left(nullptr), right(nullptr), dist(1) {}
    };

    Node* root;
    size_t _size;
    Compare comp;

    Node* merge_node(Node* a, Node* b) {
        if (a == nullptr) return b;
        if (b == nullptr) return a;
        if (comp(a->value, b->value)) {
            std::swap(a, b);
        }
        a->right = merge_node(a->right, b);
        if (a->left == nullptr || (a->right != nullptr && a->left->dist < a->right->dist)) {
            std::swap(a->left, a->right);
        }
        a->dist = (a->right == nullptr ? 0 : a->right->dist) + 1;
        return a;
    }

    Node* copy_node(Node* node) {
        if (node == nullptr) return nullptr;
        Node* new_node = new Node(node->value);
        new_node->dist = node->dist;
        try {
            new_node->left = copy_node(node->left);
            new_node->right = copy_node(node->right);
        } catch (...) {
            destroy_node(new_node->left);
            destroy_node(new_node->right);
            delete new_node;
            throw;
        }
        return new_node;
    }

    void destroy_node(Node* node) {
        if (node == nullptr) return;
        destroy_node(node->left);
        destroy_node(node->right);
        delete node;
    }

public:
    priority_queue() : root(nullptr), _size(0), comp() {}

    priority_queue(const priority_queue& other) : root(nullptr), _size(0), comp(other.comp) {
        root = copy_node(other.root);
        _size = other._size;
    }

    ~priority_queue() {
        destroy_node(root);
    }

    priority_queue& operator=(const priority_queue& other) {
        if (this == &other) return *this;
        destroy_node(root);
        root = nullptr;
        _size = 0;
        root = copy_node(other.root);
        _size = other._size;
        return *this;
    }

    const T& top() const {
        if (empty()) throw container_is_empty();
        return root->value;
    }

    void push(const T& e) {
        Node* new_node = new Node(e);
        try {
            root = merge_node(root, new_node);
        } catch (...) {
            delete new_node;
            throw;
        }
        _size++;
    }

    void pop() {
        if (empty()) throw container_is_empty();
        Node* old_root = root;
        root = merge_node(root->left, root->right);
        delete old_root;
        _size--;
    }

    size_t size() const {
        return _size;
    }

    bool empty() const {
        return root == nullptr;
    }

    void merge(priority_queue& other) {
        if (this == &other) return;
        root = merge_node(root, other.root);
        _size += other._size;
        other.root = nullptr;
        other._size = 0;
    }
};

}

#endif
