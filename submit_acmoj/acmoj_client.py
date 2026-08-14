#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ACMOJ API Client Command Line Tool - C++ File Submission Version v2.2

Usage Examples:
1. Submit C++ source file:
   python3 acmoj_client.py --token ${ACMOJ_TOKEN} submit --problem-id ${ACMOJ_PROBLEM_ID} --language cpp --code-file .cpp/.hpp/.h
   The returned result contains submission_id information, please save it for subsequent status queries

2. Query submission status:
   python3 acmoj_client.py --token ${ACMOJ_TOKEN} status --submission-id <your_submission_id>
   Note: Evaluation takes time, it's recommended to wait 10 seconds before querying status
   For example, if the returned result shows "status": "compiling" or "status": "pending", 
   it means the evaluation is still in progress or queued, please check again later

3. Abort submission:
   python3 acmoj_client.py --token ${ACMOJ_TOKEN} abort --submission-id <your_submission_id>
   Abort the evaluation of the specified submission
"""

import requests
import json
import time
import argparse
import os
from typing import Dict, Any, Optional
from datetime import datetime


class ACMOJClient:
    def __init__(self, access_token: str):
        self.api_base = "https://acm.sjtu.edu.cn/OnlineJudge/api/v1"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "ProjDevBench/20260204 ACMOJ-Python-Client/2.2"
        }

        self.submission_log_file = '/workspace/submission_ids.log'
        

    def _make_request(self, method: str, endpoint: str, data: Dict[str, Any] = None, 
                     params: Dict[str, Any] = None) -> Optional[Dict]:
        url = f"{self.api_base}{endpoint}"
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=self.headers, params=params, timeout=int(os.environ.get("ACMOJ_TIMEOUT", "60")))
            elif method.upper() == "POST":
                response = requests.post(url, headers=self.headers, data=data, timeout=int(os.environ.get("ACMOJ_TIMEOUT", "60")))
            else:
                print(f"Unsupported HTTP method: {method}")
                return None

            if response.status_code == 204:
                return {"status": "success", "message": "Operation successful"}

            response.raise_for_status()
            
            if response.content:
                return response.json()
            else:
                return {"status": "success"}

        except requests.exceptions.RequestException as e:
            print(f"API Request failed: {e}")
            if 'response' in locals() and response:
                print(f"Response text: {response.text}")
            return None

    def _save_submission_id(self, submission_id):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = {
                "timestamp": timestamp,
                "submission_id": submission_id
            }
            
            with open(self.submission_log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
            
            print(f"✅ Submission ID {submission_id} saved to {self.submission_log_file}")
        except Exception as e:
            print(f"⚠️ Warning: Failed to save submission ID: {e}")

    def submit_git(self, problem_id: int, git_url: str) -> Optional[Dict]:
        data = {"language": "git", "code": git_url}
        result = self._make_request("POST", f"/problem/{problem_id}/submit", data=data)
        if result and 'id' in result:
            self._save_submission_id(result['id'])

        return result

    def submit_code(self, problem_id: int, language: str, code: str) -> Optional[Dict]:
        """Submit source code directly."""
        data = {"language": language, "code": code}
        result = self._make_request("POST", f"/problem/{problem_id}/submit", data=data)
        if result and 'id' in result:
            self._save_submission_id(result['id'])
        return result

    def get_submission_detail(self, submission_id: int) -> Optional[Dict]:
        return self._make_request("GET", f"/submission/{submission_id}")

    def abort_submission(self, submission_id: int) -> Optional[Dict]:
        return self._make_request("POST", f"/submission/{submission_id}/abort")


def main():
    parser = argparse.ArgumentParser(description="ACMOJ API Command Line Client")
    parser.add_argument("--token", help="ACMOJ Access Token", 
                       default=os.environ.get("ACMOJ_TOKEN"))
    
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Submit C++ source file
    submit_parser = subparsers.add_parser("submit", help="Submit a C++ source file")
    submit_parser.add_argument("--problem-id", type=int, required=True, help="Problem ID")
    submit_parser.add_argument("--language", type=str, required=True,
                               help="Programming language (e.g., cpp, c, python)")
    submit_parser.add_argument("--code-file", type=str, required=True,
                               help="Path to the source code file")

    # Sub-command for checking submission status
    status_parser = subparsers.add_parser("status", help="Check submission status")
    status_parser.add_argument("--submission-id", type=int, required=True, help="Submission ID")

    # Sub-command for aborting submission
    abort_parser = subparsers.add_parser("abort", help="Abort submission evaluation")
    abort_parser.add_argument("--submission-id", type=int, required=True, help="Submission ID")

    args = parser.parse_args()

    if not args.token:
        print("Error: Access token not provided. Use --token or set ACMOJ_TOKEN environment variable.")
        return

    client = ACMOJClient(args.token)

    if args.command == "submit":
        try:
            with open(args.code_file, 'r', encoding='utf-8') as f:
                code_text = f.read()
        except FileNotFoundError:
            print(f"Error: Code file not found at {args.code_file}")
            exit(1)
        except Exception as e:
            print(f"Error: Failed to read code file: {e}")
            exit(1)

        result = client.submit_code(args.problem_id, args.language, code_text)

    elif args.command == "status":
        result = client.get_submission_detail(args.submission_id)
    elif args.command == "abort":
        result = client.abort_submission(args.submission_id)

    if result:
        print(json.dumps(result))
    else:
        # Exit with a non-zero status code to indicate failure to shell scripts
        exit(1)


if __name__ == "__main__":
    main()