# 🖨️ Mini-Print-Testing-Automation-Project

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green)
![Automation](https://img.shields.io/badge/QA-Automation-orange)
![CI Workflow](https://github.com/abhisakh/Mini-Print-Testing-Automation-Project/actions/workflows/ci.yml/badge.svg) *Includes Print & API tests*

![alt text](<assets/Screenshot 2026-03-15 at 00.01.12.png>)

*Python • Pytest • QA Automation • GitHub Actions CI/CD • Functional Test • Unit Test • Visual Regression Test • API Test*

---

## Table of Contents

- [Overview](#overview)
- [Project Idea](#project-idea)
- [Key Features](#key-features)
- [🔁 Automated Testing Pipeline (Git Push → CI → Test Reports)](#-automated-testing-pipeline-git-push--ci--test-reports)
  - [How It Works](#how-it-works)
  - [HTML Test Reports](#html-test-reports)
  - [CI Pipeline Overview](#ci-pipeline-overview)
  - [Workflow Files](#workflow-files)
- [Project Structure](#project-structure)
- [🧪 Testing Methodologies Implemented](#-testing-methodologies-implemented)
  - [1. Functional Testing](#1-functional-testing)
  - [2. Regression Testing](#2-regression-testing)
  - [3. API Testing](#3-api-testing)
  - [4. Visual Regression Testing](#4-visual-regression-testing)
  - [Layered Testing Strategy — Summary](#layered-testing-strategy--summary)
- [🧩 Testing Approaches Used in This Project](#-testing-approaches-used-in-this-project)
  - [1. Functional Testing](#1-functional-testing-1)
  - [2. Visual Regression Testing](#2-visual-regression-testing-1)
  - [3. API Testing](#3-api-testing-1)
  - [4. Automated Regression Testing (CI)](#4-automated-regression-testing-ci)
- [Running Tests](#running-tests)
  - [Run Print Tests](#run-print-tests)
  - [Run API Tests](#run-api-tests)
  - [Run All Tests (Wrapper)](#run-all-tests-wrapper)
- [Script Descriptions](#script-descriptions)
  - [printer.py — Print Job Simulator](#printerpy--print-job-simulator)
  - [validator.py — Output Integrity Validator](#validatorpy--output-integrity-validator)
  - [visual\_compare.py — Visual Regression Comparator](#visual_comparepy--visual-regression-comparator)
  - [api.py — Flask Print API Server](#apipy--flask-print-api-server)
  - [test\_print.py — Functional Test Suite](#test_printpy--functional-test-suite)
  - [test\_api.py — API Test Suite](#test_apipy--api-test-suite)
  - [run\_tests.py — Full Test Suite Wrapper](#run_testspy--full-test-suite-wrapper)
- [Installation](#installation)
  - [System Dependencies](#system-dependencies)
  - [Python Dependencies](#python-dependencies)
- [Setup & Running New Tests](#setup--running-new-tests)
- [Files to Check or Modify Before Testing](#files-to-check-or-modify-before-testing)
  - [a. sample\_files/test\_document.pdf](#a-sample_filestest_documentpdf)
  - [b. reference\_output/expected\_output.pdf](#b-reference_outputexpected_outputpdf)
  - [c. printer.py](#c-printerpy)
  - [d. validator.py](#d-validatorpy)
  - [e. visual\_compare.py](#e-visual_comparepy)
  - [f. test\_print.py](#f-test_printpy)
  - [g. test\_api.py](#g-test_apipy)
  - [h. api.py](#h-apipy)
  - [i. run\_tests.py](#i-run_testspy)
- [Real-World Use Cases](#real-world-use-cases)
- [Future Roadmap: Jira Integration](#future-roadmap)

---

## Overview

A Python-based automation framework using Pytest to simulate print jobs and validate generated output files. The framework performs automated validation of printed documents including file generation, content integrity, visual layout, and API-based print simulation.

Automated tests run on every commit using GitHub Actions. The pipeline generates detailed HTML reports that can be downloaded from workflow artifacts.

[↑ Back to Contents](#table-of-contents)

---

## Project Idea

The framework automatically:

1. Send a document to a printer (or simulator)
2. Verify the output file is generated
3. Check document properties (page count, size)
4. Validate results with pytest
5. Test print workflow via API

[↑ Back to Contents](#table-of-contents)

---

## Key Features

- Automated regression testing for print pipelines
- PDF output validation: file existence, page count, layout
- API-based print job simulation
- Cross-platform support (Windows / Mac / Virtual Machines)
- Pytest-based automated testing framework
- CI/CD integration via GitHub Actions with downloadable HTML reports

[↑ Back to Contents](#table-of-contents)

---

## 🔁 Automated Testing Pipeline (Git Push → CI → Test Reports)

This project integrates Continuous Integration (CI) using GitHub Actions to automatically validate the printing system whenever code changes are pushed to the repository.

When a developer pushes new code to the repository, the GitHub Actions workflow defined in `.github/workflows/` is automatically triggered. The workflow starts a fresh Linux-based environment and performs a sequence of automated steps to verify that the software is functioning correctly.

### How It Works

First, the CI system checks out the latest version of the repository and sets up a Python environment using the specified Python version. All required dependencies listed in `requirements.txt` are then installed. System-level dependencies such as Poppler (required for PDF processing and visual comparison) are also installed to ensure the environment fully supports document validation tasks.

After the environment is prepared, the CI pipeline executes the automated Pytest test suites. These tests include:

- Functional tests for the print simulation pipeline
- Validation tests for generated PDF files (existence, integrity, page count)
- Visual regression tests comparing output documents with reference files
- API tests that interact with the Flask print service endpoint

### HTML Test Reports

During the execution of these tests, Pytest generates a detailed HTML report using the `pytest-html` plugin. This report contains structured information about the test session, including:

- List of all executed tests
- Pass / fail status for each test
- Execution time per test
- Full error traces if failures occur

Once the tests finish, the CI workflow uploads the generated HTML report as a downloadable artifact. This allows developers or QA engineers to review the complete test results directly from the GitHub Actions interface without running the tests locally.

### CI Pipeline Overview

```
Developer pushes code (git push)
          ↓
GitHub Actions workflow triggers
          ↓
Environment setup (Python + dependencies)
          ↓
Run automated Pytest test suites
          ↓
Generate HTML test report
          ↓
Upload report as workflow artifact
```

### Workflow Files

- Print Testing Workflow: `.github/workflows/ci-print.yml`
- API Testing Workflow: `.github/workflows/ci-api.yml`

Badges at the top of the repository reflect the live status of each workflow. Both workflows upload HTML reports as downloadable artifacts for detailed inspection.

This approach reflects real-world QA automation practices, where automated test pipelines continuously verify system functionality and generate traceable test reports for quality assurance and debugging.

[↑ Back to Contents](#table-of-contents)

---

## Project Structure

```text
project-root/
├── LICENSE
├── README.md
├── requirements.txt
├── printer.py              → Simulates print job (copies file)
├── validator.py            → Validates output file
├── visual_compare.py       → Compares output vs reference PDF
├── api.py                  → Flask API exposing /print endpoint
├── test_print.py           → Functional pytest test suite
├── test_api.py             → API pytest test suite
├── run_tests.py            → Wrapper to run all tests + reports
├── sample_files/
│   └── test_document.pdf   → Input document for tests
├── printed_output/
│   └── output.pdf          → Generated output
├── reference_output/
│   └── expected_output.pdf → Reference for comparison
├── assets/
│   └── style.css
└── .github/
    └── workflows/
        ├── ci-print.yml
        └── ci-api.yml
```

[↑ Back to Contents](#table-of-contents)

---

## 🧪 Testing Methodologies Implemented

This project demonstrates several testing approaches commonly used in professional software quality assurance environments. By combining multiple testing methods, the project validates the print pipeline from different perspectives, ensuring both correctness of functionality and long-term stability of the system.

### 1. Functional Testing

**Implemented in:** `test_print.py`

Functional testing is implemented through the Pytest test suite that directly interacts with the internal modules responsible for the print simulation. These tests verify that the core functionality behaves as expected.

For example, the tests ensure that a print job successfully generates an output file, that the produced PDF exists in the correct location, that it is not empty, and that the page count matches the expected document structure.

> ***Why it is called functional testing:*** The tests verify whether the core functions of the system operate according to their specifications. Each test maps directly to a specific function of the print pipeline — sending a job, generating a file, counting pages — and confirms that each function produces the correct result.

#### What is tested

- Print job execution — confirms the job runs without errors
- Output file generation — verifies the output PDF is created in the correct location
- File integrity — confirms the output is not empty
- Page count validation — checks the PDF has the expected number of pages

#### Run

```bash
pytest test_print.py -v
```

#### Example Output

```
test_print.py::test_print_job PASSED
test_print.py::test_print_file_not_empty PASSED
test_print.py::test_pdf_page_count PASSED
test_print.py::test_visual_layout PASSED
================ 4 passed in 0.05s =================
```

---

### 2. Regression Testing

**Implemented via:** `test_print.py` + `test_api.py` + GitHub Actions CI

Regression testing is incorporated through the automated execution of all tests whenever code changes occur. Each time the system is modified, the existing test suite is re-executed to ensure that previously working features still function correctly.

If a change in the printing logic breaks file generation, page counting, or other established behaviours, the tests will fail and immediately reveal the issue.

> ***Why it is called regression testing:*** Its purpose is to detect whether new code changes have caused the system to regress — that is, to break functionality that previously worked correctly. Every CI run re-validates the entire pipeline against its known-good baseline, catching regressions the moment they are introduced.

**Triggered automatically by:** `git push → GitHub Actions → full test suite execution`

---

### 3. API Testing

**Implemented in:** `test_api.py` against `api.py`

API testing is implemented by exposing the print functionality through a Flask-based REST API. Automated tests send HTTP requests to the `/print` endpoint to trigger print jobs programmatically. These tests validate that the API accepts requests correctly, processes input data, and returns a proper response after executing the print simulation.

> ***Why it is called API testing:*** The system is tested through its external interface, simulating how another service or client application would interact with the printing system. Rather than calling Python modules directly, the tests communicate with the system exclusively via HTTP — exactly as an external consumer of the API would.

#### API Endpoint

```
POST /print
```

#### Example Request

```json
{
  "filename": "sample_files/test_document.pdf"
}
```

#### Run API Tests

Start the API server first:

```bash
python api.py
```

Then run:

```bash
pytest test_api.py -v
```

#### Example Output

```
test_api.py::test_print_api PASSED
```

---

### 4. Visual Regression Testing

**Implemented in:** `visual_compare.py` → called by `test_print.py::test_visual_layout`

Visual regression testing is implemented through comparison between the generated output PDF and a predefined reference document. The system converts both documents into images and analyses them for visual differences such as layout changes, missing elements, or formatting inconsistencies.

This type of testing is especially important in print and document-rendering systems where even minor formatting changes can introduce errors that would pass all other checks undetected.

> ***Why it is called visual regression testing:*** It verifies that the visual appearance of the output has not changed unexpectedly after code modifications. Like regression testing, it guards against unintended changes — but at the visual and layout layer rather than at the functional or API layer.

#### How it works

1. Converts both the generated output and the reference PDF into images using `pdf2image`
2. Compares the images page by page at the pixel level using Pillow
3. Calculates pixel-level differences between corresponding pages
4. Returns `False` and fails the test if any visual difference is detected

**Comparison:** `printed_output/output.pdf` vs `reference_output/expected_output.pdf`

---

### Layered Testing Strategy — Summary

By integrating functional testing, regression testing, API testing, and visual regression testing within an automated Pytest framework and CI pipeline, this project reflects a layered quality assurance strategy similar to those used in real-world software testing environments:

| Testing Methodology | What It Validates | Implemented In |
|---|---|---|
| Functional Testing | Core functions work to specification | `test_print.py` |
| Regression Testing | Changes do not break existing features | All tests via GitHub Actions CI |
| API Testing | External interface behaves correctly | `test_api.py` + `api.py` |
| Visual Regression Testing | Output layout unchanged after changes | `visual_compare.py` |

Each methodology targets a different failure mode. Together they ensure that the print pipeline is correct internally, stable across changes, reliable externally, and visually consistent in its output.

[↑ Back to Contents](#table-of-contents)

---

## 🧩 Testing Approaches Used in This Project

This section provides additional context on how each testing approach is applied within this project, including the specific files involved and the system layers each approach targets.

### 1. Functional Testing

Directly tests the internal Python modules of the print pipeline. Tests call `printer.py`, `validator.py`, and `visual_compare.py` without any intermediary layer.

**Implemented in:** `test_print.py`

### 2. Visual Regression Testing

Converts PDFs to images and compares them pixel by pixel against a reference. Catches layout regressions that pass all other checks — such as shifted elements, font changes, or broken margins.

**Implemented in:** `visual_compare.py` → called by `test_print.py::test_visual_layout`

### 3. API Testing

Sends real HTTP POST requests to the Flask `/print` endpoint and validates the response. Tests the system exactly as an external client would, covering the integration layer that direct module tests do not reach.

**Implemented in:** `test_api.py` against `api.py`

### 4. Automated Regression Testing (CI)

Every `git push` triggers GitHub Actions to re-run the full test suite automatically. This ensures that no code change silently breaks existing behaviour. HTML reports are uploaded as downloadable artifacts after each run.

**Implemented via:** `.github/workflows/ci-print.yml` and `.github/workflows/ci-api.yml`

[↑ Back to Contents](#table-of-contents)

---

## Running Tests

### Run Print Tests

```bash
pytest test_print.py -v
```

Generate HTML report:

```bash
pytest --html=Pytest-Report-Print-Testing-Automation.html
```

### Run API Tests

Make sure `api.py` is running locally:

```bash
python api.py
```

Then run:

```bash
pytest test_api.py -v
```

Generate HTML report:

```bash
pytest --html=Pytest-Report-API-Testing.html
```

### Run All Tests (Wrapper)

```bash
python run_tests.py
```

[↑ Back to Contents](#table-of-contents)

---

## Script Descriptions

This section describes the purpose, internal behaviour, inputs, outputs, and role in the pipeline for every script in the project.

### printer.py — Print Job Simulator

**Purpose:** Simulates the act of sending a document to a printer.

**How it works:**
Instead of communicating with a real hardware printer, this script copies the input PDF file from the `sample_files/` directory into the `printed_output/` directory, naming it `output.pdf`. This simulates what a printer driver or print server would do when it receives and processes a document.

**Input:** `sample_files/test_document.pdf`
**Output:** `printed_output/output.pdf`

**Role in pipeline:**
This is the first step in the test pipeline. Every test in `test_print.py` calls this script before performing any validation. If `printer.py` fails, all downstream tests will also fail.

**Real-world equivalent:**
In a production environment this could be replaced with a real printer driver call, a network print server API, or a digital printing system SDK.

---

### validator.py — Output Integrity Validator

**Purpose:** Validates that the output PDF produced by `printer.py` is correct and complete.

**How it works:**
The validator performs three sequential checks on the generated output file:

1. File existence check — confirms that `printed_output/output.pdf` was actually created
2. File size check — confirms that the file is not empty (size > 0 bytes)
3. Page count check — opens the PDF and verifies the number of pages matches the expected value

**Input:** `printed_output/output.pdf`
**Output:** Boolean result — `True` if all checks pass, `False` or exception if any check fails

**Role in pipeline:**
Acts as the integrity gate. It is called by `test_print.py` after `printer.py` runs. If the output file is missing, empty, or has the wrong page count, the validator raises an error and the corresponding test fails immediately, preventing any further validation steps from running on an invalid file.

**Real-world equivalent:**
In production print pipelines, output validation is a standard quality gate step used to catch failed print jobs, truncated files, or rendering errors before documents are delivered or archived.

---

### visual\_compare.py — Visual Regression Comparator

**Purpose:** Detects visual layout regressions by pixel-level comparison of the generated output against a known-correct reference PDF.

**How it works:**

1. Converts both PDFs into images using `pdf2image` (which requires Poppler to be installed)
2. Compares the images page by page at the pixel level using Pillow
3. Calculates the difference between corresponding pixels across both documents
4. Returns `False` if any pixel difference exceeds the threshold, indicating a layout change

**Input:** `printed_output/output.pdf` vs `reference_output/expected_output.pdf`
**Output:** `True` if the documents match visually, `False` if a layout difference is detected

**Role in pipeline:**
Serves as the visual quality gate. It catches rendering regressions that would pass both the existence check and page count check — such as shifted text blocks, missing images, changed fonts, broken layouts, or incorrect margins. Called by the `test_visual_layout` test case in `test_print.py`.

**Real-world equivalent:**
Visual regression testing is widely used in document management systems, publishing pipelines, and print-on-demand platforms to ensure that layout changes do not silently degrade document quality.

---

### api.py — Flask Print API Server

**Purpose:** Exposes the print pipeline as a REST API, allowing external clients to trigger print jobs over HTTP.

**How it works:**
This script starts a Flask web server that listens for incoming HTTP POST requests on the `/print` endpoint. When a request is received, the API:

1. Reads the filename from the JSON request body
2. Calls `printer.py` to simulate the print job
3. Calls `validator.py` to verify the output
4. Returns a JSON response indicating success or failure

**Endpoint:** `POST /print`

**Example request body:**
```json
{
  "filename": "sample_files/test_document.pdf"
}
```

**Input:** JSON body with `filename` field
**Output:** JSON response with status and message

**Role in pipeline:**
Must be running locally before any API tests are executed. It is the system under test for `test_api.py`. This script enables system-level and integration testing by exposing the same internal print logic through an external interface.

**Real-world equivalent:**
Cloud print services, document processing platforms, and enterprise print management systems routinely expose print functionality through REST APIs to allow integration with external applications and workflows.

---

### test\_print.py — Functional Test Suite

**Purpose:** The primary pytest test file for direct functional testing of the print pipeline modules.

**How it works:**
Each test function in this file calls the internal Python modules directly, without going through the API. The four test cases cover the full pipeline from print job execution to visual layout verification:

- **`test_print_job`** — Calls `printer.py` and asserts that the function completes without raising an exception. Verifies the print job itself runs successfully.
- **`test_print_file_not_empty`** — Checks that the output file exists and has a non-zero file size. Catches cases where the print job ran but produced an empty or missing file.
- **`test_pdf_page_count`** — Opens the output PDF and asserts that the page count matches the expected value. Detects truncated or incorrectly rendered documents.
- **`test_visual_layout`** — Calls `visual_compare.py` to perform pixel-level comparison between the generated output and the reference PDF. Detects any visual layout regressions.

**Run command:**
```bash
pytest test_print.py -v
```

**Role in pipeline:**
This is the entry point for all functional regression testing and is the file executed by the `ci-print.yml` GitHub Actions workflow on every push.

---

### test\_api.py — API Test Suite

**Purpose:** Validates the print functionality at the system level by sending real HTTP requests to the running Flask API and asserting the responses.

**How it works:**
Using the `requests` library, this test file sends a POST request to the `/print` endpoint with a JSON payload containing the test document filename. It then asserts that the API returns the expected HTTP status code and a success response body.

- **`test_print_api`** — Sends `POST /print` with the test filename, asserts HTTP 200, and validates the JSON response confirms the print job succeeded.

**Prerequisite:** `api.py` must be running locally before executing this test suite. If the server is not running, all tests will fail with a connection error.

**Run command:**
```bash
python api.py        # start server first
pytest test_api.py -v
```

**Role in pipeline:**
Executed by the `ci-api.yml` GitHub Actions workflow. Tests the same underlying print functionality as `test_print.py` but through the external HTTP interface, providing system-level and integration test coverage as a separate layer.

---

### run\_tests.py — Full Test Suite Wrapper

**Purpose:** A convenience wrapper script that runs both the functional and API test suites in sequence and generates HTML reports for each.

**How it works:**
Internally calls pytest programmatically (or via subprocess) with the appropriate arguments for each test file and the `--html` flag to produce a named report file. Runs `test_print.py` first, then `test_api.py`, and saves both HTML reports to the project root.

**Output reports:**
- `Pytest-Report-Print-Testing-Automation.html`
- `Pytest-Report-API-Testing.html`

**Run command:**
```bash
python run_tests.py
```

**Role in pipeline:**
Designed for local full-suite regression runs where a developer wants to replicate the complete CI pipeline locally in a single command, including report generation. Not used by the CI workflows directly — those call pytest individually per suite.

[↑ Back to Contents](#table-of-contents)

---

## Installation

### System Dependencies

This project requires Poppler for PDF image conversion.

**macOS:**
```bash
brew install poppler
```

**Ubuntu:**
```bash
sudo apt install poppler-utils
```

**Windows:**
Download Poppler from: https://github.com/oschwartz10612/poppler-windows/releases

### Python Dependencies

`requirements.txt`:

```
pytest>=8.0
pypdf>=4.0
pdf2image>=1.17
pillow>=10.0
flask
pytest-html
```

Install:

```bash
pip install -r requirements.txt
```

[↑ Back to Contents](#table-of-contents)

---

## Setup & Running New Tests

1. Clone or download the project
```bash
git clone <repository-url>
cd <project-folder>
```

2. Create a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install requirements (see [Installation](#installation) section above)

4. Check or modify required files (see [Files to Check or Modify Before Testing](#files-to-check-or-modify-before-testing) section below)

5. Run tests (see [Running Tests](#running-tests) section above)

[↑ Back to Contents](#table-of-contents)

---

## Files to Check or Modify Before Testing

Before running tests, review the following files. Each plays a specific role in the test pipeline. Modify only the ones relevant to your changes.

### a. sample\_files/test\_document.pdf

**Location:** `sample_files/test_document.pdf`

**What it contains:**
The input PDF document that is fed into the print pipeline during testing. This is the file that `printer.py` processes and sends to the output folder.

**Significance:**
This is the starting point of every test run. All tests depend on this file being a valid, readable PDF. If it is missing or corrupted, the entire test suite will fail.

**When to modify:**
- You want to test with a different document
- You are validating behaviour with specific page counts or layouts
- You are simulating a real-world print job with a production-like document

---

### b. reference\_output/expected\_output.pdf

**Location:** `reference_output/expected_output.pdf`

**What it contains:**
The known-correct reference PDF that represents the expected output of a successful print job. It acts as the ground truth for visual and structural comparison.

**Significance:**
Used by `visual_compare.py` to detect layout regressions. The test passes only if the generated output matches this reference pixel-by-pixel. If this file is outdated, visual tests will give false failures.

**When to modify:**
- The expected output layout or content has intentionally changed
- You have updated the print pipeline and confirmed the new output is correct
- You are setting up the project for the first time with a new document

> **Important:** Always verify the new reference visually before committing it, as this file defines what "correct" means for all future test runs.

---

### c. printer.py

**Location:** `printer.py`

**What it contains:**
The main script that simulates sending a print job. It reads the input file from `sample_files/` and writes the output to `printed_output/output.pdf`. In real systems this would interface with a printer driver, print server, or digital printer simulator.

**Significance:**
This is the core of the print pipeline. Every functional test calls this script as the first step. If the output path, filename, or logic changes here, both `validator.py` and `visual_compare.py` will be affected.

**When to modify:**
- The printing logic changes (e.g. format conversion, compression)
- The output file path or filename changes
- You are connecting to a real printer driver or print server

---

### d. validator.py

**Location:** `validator.py`

**What it contains:**
The validation module that checks the generated output file. It verifies three things: (1) the output file exists, (2) the file is not empty, and (3) the page count matches expectations.

**Significance:**
This is the integrity gate of the pipeline. Tests that call the validator will fail immediately if the output is missing, empty, or has an unexpected page count — catching the most common print failures early.

**When to modify:**
- You need to check additional properties (e.g. file size, metadata, orientation)
- The expected page count changes
- The output format changes and new validation logic is required

---

### e. visual\_compare.py

**Location:** `visual_compare.py`

**What it contains:**
The visual regression script. It converts both the generated output and the reference PDF into images, then compares them pixel by pixel. Returns `False` if any layout difference is detected.

**Comparison:** `printed_output/output.pdf` vs `reference_output/expected_output.pdf`

**Significance:**
Catches rendering regressions that would not be found by file-existence or page-count checks alone — such as shifted text, missing images, font changes, or layout breaks. This is the visual quality gate of the pipeline.

**When to modify:**
- The PDF comparison method needs to change (e.g. tolerance threshold, DPI setting)
- You want to compare individual pages rather than the whole document
- You are adding support for image or non-PDF format comparison

---

### f. test\_print.py

**Location:** `test_print.py`

**What it contains:**
The main pytest test file for functional testing. Contains four test cases that together cover the complete print pipeline:

- `test_print_job` — verifies the print job runs without errors
- `test_print_file_not_empty` — checks the output file is non-empty
- `test_pdf_page_count` — validates the page count of the output
- `test_visual_layout` — compares the output against the reference PDF

**Significance:**
This is the primary test file executed by pytest and by the CI pipeline. It is the entry point for all functional regression testing of the print pipeline.

**When to modify:**
- New test cases need to be added
- Test inputs or expected values change
- Validation logic or assertions need updating

---

### g. test\_api.py

**Location:** `test_api.py`

**What it contains:**
The pytest test file for API-level testing. Sends HTTP POST requests to the running Flask API and validates the response. Tests the same print pipeline but through the external REST interface rather than calling Python modules directly.

**Significance:**
Validates the system from the outside, exactly as an external client or service would. Ensures the API contract (endpoint, request format, response) is stable and correct — separate from the internal implementation.

**When to modify:**
- The API endpoint or request/response format changes
- New API test cases are added
- Authentication or headers are introduced to the API

---

### h. api.py

**Location:** `api.py`

**What it contains:**
The Flask application that exposes the print pipeline as a REST API. Defines the `POST /print` endpoint which accepts a filename, triggers the print job, runs validation, and returns a JSON response.

**Significance:**
Must be running locally before any API tests are executed. Acts as the server under test. If this file is not started before running `test_api.py`, all API tests will fail with a connection error.

**When to modify:**
- New API endpoints are added
- The response format or status codes change
- Error handling or authentication logic is updated

---

### i. run\_tests.py

**Location:** `run_tests.py`

**What it contains:**
An optional wrapper script that runs all tests (both functional and API) in sequence and automatically generates HTML reports for each suite.

**Significance:**
Provides a single command to execute the full test suite and produce reports, useful for local regression runs and for reviewing results without accessing the CI pipeline.

**When to modify:**
- You want to change the report filenames or output paths
- You need custom test execution order or additional pre/post steps
- You are adding new test files that should be included in the full run

[↑ Back to Contents](#table-of-contents)

---

## Real-World Use Cases

This framework simulates automated validation workflows used in industry QA and demonstrates multiple layers of testing highly valued in QA engineering roles.

- Printer driver validation
- Digital print pipeline testing
- Automated regression testing of document rendering systems
- API testing for document print job submission
- Continuous Integration support for QA teams

[↑ Back to Contents](#table-of-contents)

---
<a id="future-roadmap"></a>
## 🚀 Future Roadmap: Jira Integration

Jira Integration for Automated Defect Reporting
To align with professional Agile workflows, this project is designed to integrate with the Jira Cloud API. This allows for:

- Automated Ticket Creation: If a regression test (like test_visual_layout) fails, a Jira issue is automatically created with the full error trace.
- Traceability: Mapping Pytest Test IDs to Jira User Stories to ensure all software functional specifications are validated.
- Status Updates: Automatically transitioning Jira tickets from "In Progress" to "Done" when a previously failing test passes in the CI/CD pipeline.


[↑ Back to Contents](#table-of-contents)
