# 🖨️ Mini-Print-Testing-Automation-Project
A Python-based automation framework using Pytest to simulate print jobs and validate generated output files. Implemented automated checks for file creation, content integrity, and document properties, supporting regression testing of print workflows.

## Project Idea
Automatically:

1. Send a document to a printer (or simulator)
2. Verify the output file is generated
3. Check document properties (page count, size)
4. Validate results with pytest

This simulates automated regression testing for print pipelines.

---

## 1️⃣ Project Structure

Folder structure:

```python
.
│
├── printer.py
├── validator.py
├── visual_compare.py
├── test_print.py
│
├── reference_output/
│     expected_output.pdf
│
├── printed_output/
│
└── sample_files/
      test_document.pdf
```

---

## 2️⃣ Printer Script

<mark>printer.py</mark>

This simulates sending a print job.
Instead of a real printer, we simulate printing by copying the file.

In real systems this could be:
- printer driver
- print server
- digital printer simulator.

---

## 3️⃣ Output Validation Script

<mark>validator.py</mark>

This script checks:
- file exists
- file is not empty
- correct page count

---

## 4️⃣ Visual Comparison Script

<mark>visual_compare.py</mark>

1️. Converts PDFs → images
2️. Compares pixel differences
3️. Returns False if layout changed

---

## 5️⃣ Pytest Test Suite

<mark>test_print.py</mark>

This script automate the pytest

---

## 5️⃣ Install Requirements

<mark>requirements.txt</mark>
```python
pytest
pypdf
```
Install

```python
pip install -r requirements.txt
```
---

## 6️⃣ Run Tests

Run:
```python
pytest test_print.py -v
```
Example Output:
```python
test_print.py::test_print_job PASSED
test_print.py::test_print_file_not_empty PASSED
test_print.py::test_pdf_page_count PASSED
```

---

## 7️⃣ Significance

- ✔ simulate print workflows
- ✔ automate validation using pytest
- ✔ verify print output files
- ✔ build automated regression tests












