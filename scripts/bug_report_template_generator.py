#!/usr/bin/env python3
"""Generate a clean bug report template."""


def generate_bug_report_template() -> str:
    return """# Bug Report

## Title

Clear, specific summary of the issue.

## Environment

- Application:
- Browser/Device:
- Test Environment:
- Build/Version:

## Preconditions

List any setup required before reproducing the issue.

## Steps to Reproduce

1.
2.
3.

## Expected Result

Describe the expected behavior.

## Actual Result

Describe the actual behavior.

## Severity

Low / Medium / High / Critical

## Priority

Low / Medium / High / Critical

## Impact

Explain who or what is affected.

## Evidence

- Screenshot:
- Video:
- Logs:
- Test case:
- API response:
- SQL query:

## Notes

Add any additional details, suspected root cause, or related tickets.
"""


def main() -> None:
    print(generate_bug_report_template())


if __name__ == "__main__":
    main()
