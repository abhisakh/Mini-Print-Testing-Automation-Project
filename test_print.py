from printer import send_print_job
from validator import file_exists, file_not_empty, get_page_count
from visual_compare import compare_pdfs

INPUT_FILE = "sample_files/test_document.pdf"
REFERENCE = "reference_output/expected_output.pdf"


def test_print_job():
    output = send_print_job(INPUT_FILE)

    assert file_exists(output)


def test_print_file_not_empty():
    output = send_print_job(INPUT_FILE)

    assert file_not_empty(output)


def test_pdf_page_count():
    output = send_print_job(INPUT_FILE)

    assert get_page_count(output) == 11


def test_visual_layout():
    output = send_print_job(INPUT_FILE)

    assert compare_pdfs(output, REFERENCE)