#!/usr/bin/env python3
"""Summarize JSON test results for release-readiness review."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def summarize_results(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    tests = data.get("tests", [])

    status_counts: Counter[str] = Counter(test.get("status", "unknown").lower() for test in tests)
    failed_tests = [
        {
            "name": test.get("name", "Unnamed test"),
            "failure_category": test.get("failure_category", "unclassified"),
            "message": test.get("message", ""),
        }
        for test in tests
        if test.get("status", "").lower() == "failed"
    ]

    return {
        "total": len(tests),
        "status_counts": dict(status_counts),
        "failed_tests": failed_tests,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize JSON test result output.")
    parser.add_argument("results_file", type=Path, help="Path to JSON test results.")
    args = parser.parse_args()

    summary = summarize_results(args.results_file)

    print("Test Result Summary")
    print("-------------------")
    print(f"Total: {summary['total']}")
    for status, count in sorted(summary["status_counts"].items()):
        print(f"{status.title()}: {count}")

    if summary["failed_tests"]:
        print("\nFailed Tests")
        print("------------")
        for failed in summary["failed_tests"]:
            print(f"- {failed['name']} [{failed['failure_category']}]: {failed['message']}")


if __name__ == "__main__":
    main()
