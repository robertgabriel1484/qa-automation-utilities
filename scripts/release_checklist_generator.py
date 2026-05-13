#!/usr/bin/env python3
"""Generate a release-readiness checklist for QA review."""

from __future__ import annotations

from datetime import date


def generate_release_checklist(release_name: str = "Release Candidate") -> str:
    today = date.today().isoformat()

    return f"""# Release Readiness Checklist

Release: {release_name}
Date: {today}

## QA Validation

- [ ] Smoke tests completed
- [ ] Regression tests completed
- [ ] API tests completed
- [ ] Data validation checks completed
- [ ] High-priority defects reviewed
- [ ] Blocker/Critical defects resolved or approved for release
- [ ] Failed tests reviewed and explained
- [ ] Test evidence attached or linked

## Defect Review

- [ ] Open defects reviewed
- [ ] Fixed defects re-tested
- [ ] Regression impact reviewed
- [ ] Known issues documented

## Release Decision

- [ ] QA recommendation documented
- [ ] Product/Engineering stakeholders informed
- [ ] Release notes reviewed
- [ ] Go/No-Go decision captured
"""


def main() -> None:
    print(generate_release_checklist())


if __name__ == "__main__":
    main()
