# QA Automation Utilities

A QA/SDET portfolio project containing practical Python utilities that support common QA work: parsing logs, summarizing test results, validating CSV data, generating release checklists, creating bug report templates, and classifying failed tests.

## Project Purpose

This project demonstrates:

- Python scripting for QA automation support
- Log parsing and failure extraction
- Test report summarization
- CSV/data validation
- Release checklist generation
- Bug report template generation
- Failed test classification
- Command-line utility structure
- Unit tests for utility scripts
- GitHub Actions CI execution

## Why This Matters

QA engineers often save teams time by automating repetitive support tasks. This repo shows small, practical scripts that can reduce manual effort around test review, release readiness, defect documentation, and data validation.

## Tech Stack

- Python 3.11+
- Standard library only
- unittest
- GitHub Actions

## Utilities Included

```text
scripts/
  log_parser.py
  test_report_summarizer.py
  csv_data_validator.py
  release_checklist_generator.py
  bug_report_template_generator.py
  failed_test_classifier.py
```

## Sample Data

```text
sample_data/
  sample_app.log
  sample_test_results.json
  sample_invoices.csv
```

## How to Run Locally

Run all unit tests:

```bash
python -m unittest discover tests
```

Parse a log file:

```bash
python scripts/log_parser.py sample_data/sample_app.log
```

Summarize test results:

```bash
python scripts/test_report_summarizer.py sample_data/sample_test_results.json
```

Validate CSV data:

```bash
python scripts/csv_data_validator.py sample_data/sample_invoices.csv
```

Generate a release checklist:

```bash
python scripts/release_checklist_generator.py
```

Generate a bug report template:

```bash
python scripts/bug_report_template_generator.py
```

Classify failed tests:

```bash
python scripts/failed_test_classifier.py sample_data/sample_test_results.json
```

## CI/CD

This project is designed to run through GitHub Actions using:

```text
.github/workflows/python-utilities-tests.yml
```

## Portfolio Notes

My production QA background includes test planning, defect analysis, root-cause investigation, regression reporting, data validation, release readiness, and AI-assisted QA workflows.

This repo demonstrates how I use scripting to support practical QA work and reduce repetitive manual effort.
