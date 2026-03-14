from printer import send_print_job
from validator import file_exists, file_not_empty, get_page_count

INPUT_FILE = "sample_files/test_document.pdf"


def test_print_job():
    output = send_print_job(INPUT_FILE)

    assert file_exists(output)


def test_print_file_not_empty():
    output = send_print_job(INPUT_FILE)

    assert file_not_empty(output)


def test_pdf_page_count():
    output = send_print_job(INPUT_FILE)

    assert get_page_count(output) == 11
