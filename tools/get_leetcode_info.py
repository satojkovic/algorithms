#!/usr/bin/env python3
"""
Fetch LeetCode solved problem info and save to JSON.

Usage:
    export LEETCODE_SESSION="your_session_cookie"
    python tools/get_leetcode_info.py [output_path]

Output defaults to tools/leetcode_info.json.

How to get LEETCODE_SESSION:
    1. Log in to LeetCode in your browser
    2. Open DevTools > Application > Cookies > https://leetcode.com
    3. Copy the value of LEETCODE_SESSION
    4. Run: export LEETCODE_SESSION='<value>'
"""

import json
import os
import sys
import time

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"
DEFAULT_OUTPUT = os.path.join(os.path.dirname(__file__), "leetcode_info.json")

QUERY = """
query problemsetQuestionList($limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: ""
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      frontendQuestionId: questionFrontendId
      title
      titleSlug
      difficulty
      topicTags {
        name
        slug
      }
      status
    }
  }
}
"""


def get_csrf_token(session_cookie: str) -> str:
    resp = requests.get(
        "https://leetcode.com",
        cookies={"LEETCODE_SESSION": session_cookie},
        timeout=10,
    )
    return resp.cookies.get("csrftoken", "")


def fetch_solved_problems(session_cookie: str) -> dict:
    csrf_token = get_csrf_token(session_cookie)
    cookies = {
        "LEETCODE_SESSION": session_cookie,
        "csrftoken": csrf_token,
    }
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "x-csrftoken": csrf_token,
    }

    all_problems = {}
    skip = 0
    limit = 100

    while True:
        payload = {
            "query": QUERY,
            "variables": {
                "limit": limit,
                "skip": skip,
                "filters": {"status": "AC"},
            },
        }
        resp = requests.post(
            GRAPHQL_URL,
            json=payload,
            cookies=cookies,
            headers=headers,
            timeout=10,
        )
        resp.raise_for_status()

        data = resp.json()["data"]["problemsetQuestionList"]
        total = data["total"]
        questions = data["questions"]

        for q in questions:
            num = q["frontendQuestionId"]
            all_problems[num] = {
                "title": q["title"],
                "slug": q["titleSlug"],
                "difficulty": q["difficulty"].lower(),
                "tags": [tag["slug"] for tag in q["topicTags"]],
            }

        skip += limit
        fetched = min(skip, total)
        print(f"Fetched {fetched}/{total} problems...")

        if skip >= total:
            break

        time.sleep(0.5)

    return all_problems


def main():
    session_cookie = os.environ.get("LEETCODE_SESSION")
    if not session_cookie:
        print("Error: LEETCODE_SESSION environment variable is not set.")
        print()
        print("How to set it:")
        print("  1. Log in to LeetCode in your browser")
        print("  2. Open DevTools > Application > Cookies > https://leetcode.com")
        print("  3. Copy the value of LEETCODE_SESSION")
        print("  4. export LEETCODE_SESSION='<value>'")
        sys.exit(1)

    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT

    print("Fetching solved problems from LeetCode...")
    problems = fetch_solved_problems(session_cookie)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(problems, f, ensure_ascii=False, indent=2)

    print(f"\nDone. Saved {len(problems)} problems to {output_path}")


if __name__ == "__main__":
    main()
