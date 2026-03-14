# 🖨️ Mini-Print-Testing-Automation-Project

## Project Idea
Automatically:

1️⃣ Send a document to a printer (or simulator)
2️⃣ Verify the output file is generated
3️⃣ Check document properties (page count, size)
4️⃣ Validate results with pytest

This simulates automated regression testing for print pipelines.

---

## 1️⃣ Project Structure

Folder structure:
```python
print-testing-automation/
│
├── printer.py
├── validator.py
├── test_print.py
├── sample_files/
│      test_document.pdf
│
└── requirements.txt
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

3️⃣ Output Validation Script

validator.py

This script checks:
- file exists
- file is not empty
- correct page count






