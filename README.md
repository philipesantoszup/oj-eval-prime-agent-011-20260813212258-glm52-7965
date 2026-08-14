# STLite Priority Queue

**ACMOJ Problem ID**: 2623

## Table of Contents

- [STLite Priority Queue](#stlite-priority-queue)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Assignment Description](#assignment-description)
    - [Grade Composition](#grade-composition)
  - [Assignment Requirements](#assignment-requirements)
    - [Required Functions](#required-functions)
    - [Important Notes](#important-notes)
    - [Exception Handling](#exception-handling)
  - [Test Data](#test-data)
  - [Per-Testcase Resource Limits](#per-testcase-resource-limits)
  - [Submission Requirements](#submission-requirements)
    - [File Descriptions](#file-descriptions)
    - [Submission Guidelines](#submission-guidelines)
    - [Allowed Libraries](#allowed-libraries)
    - [Academic Integrity](#academic-integrity)

## Introduction

This assignment requires you to implement a `priority_queue` container similar to `std::priority_queue` in the C++ Standard Library. You need to implement a max-heap data structure with efficient merge operations.

## Assignment Description

### Grade Composition

| Component | Percentage |
| :--: | :--: |
| OJ Score | 80% |
| Code Review | 20% |

## Assignment Requirements

### Required Functions

You only need to submit the contents of `priority_queue.hpp`. You need to complete the following:

- **Constructors** (two types)
- **Destructor**
- **Assignment operator** (`operator=`)
- **Get top element** (`top`)
- **Enqueue element** (`push`)
- **Dequeue top element** (`pop`)
- **Queue size** (`size`)
- **Check if empty** (`empty`)
- **Merge queues** (`merge`)

For specific details, refer to the provided `priority_queue.hpp` framework.

### Important Notes

- **Allowed Headers**: You can only use the header files provided in the starter code framework.

- **Merge Complexity**: The `merge` operation complexity cannot exceed O(log n). This means you may need to implement a mergeable heap (e.g., leftist heap, binomial heap, pairing heap, Fibonacci heap).

- **Memory Leak Testing**: There are test cases that check for memory leaks.

- **Robustness Testing**: Your program will be subject to robustness testing.

### Exception Handling

The `Compare` function may throw exceptions for certain data. When this happens, you should terminate the ongoing operation and restore the heap to its original state.

Specifically, we will use an unstable `cmp` to check your `priority_queue` behavior during `push`, `pop`, and `merge` operations:

- **If `cmp` does not throw an exception**: We guarantee that `cmp` returns the correct result. You should handle it normally.

- **If `cmp` throws an exception during an operation**: You need to:
  1. Terminate the current operation
  2. Restore the current `priority_queue` to its state before the operation (for `merge`, there are two queues to restore)
  3. Throw a `runtime_error` exception

## Test Data

Public test cases for local testing are provided at:
- `./data/` - Test files organized by test groups (one through six)
- Some tests include `.memcheck` variants for memory leak detection

Each test directory contains:
- `code.cpp` - Test driver code
- `answer.txt` - Expected output

## Per-Testcase Resource Limits

- **Time Limit (per test case)**: 1000 ms (min), 15000 ms (max)
- **Memory Limit (per test case)**: 512 MiB
- **Disk Usage**: Disk access is not permitted

## Submission Requirements

### File Descriptions

The assignment package includes:

- **`priority_queue.hpp`**: The only file you need to implement and submit to OJ.

- **`src/exceptions.hpp`** and **`src/utility.hpp`**: Auxiliary files (**DO NOT MODIFY**).

- **`data/` directory**: Contains multiple sets of test data in separate subdirectories.

### Submission Guidelines

- For ACMOJ problem 2623, submit only the contents of `priority_queue.hpp`
- Do not modify the provided interface framework
- Ensure your implementation meets time and memory limits
- Ensure `merge` operation is O(log n) complexity
- Use C++

### Allowed Libraries

**IMPORTANT**: You can only use the header files provided in the starter code framework.

### Academic Integrity

If during Code Review any violations are found (including but not limited to using other header files, using unconventional methods to pass test cases, or `merge` complexity exceeding O(log n)), in principle your final score will be **0 points**.

---

**For detailed interface specifications, please refer to the comments in `priority_queue.hpp`.**
