import requests
import os

BASE_URL = "http://127.0.0.1:5000"

def test_print_api():
    file_path = "sample_files/test_document.pdf"
    assert os.path.exists(file_path)

    response = requests.post(f"{BASE_URL}/print", json={"filename": file_path})

    # Check HTTP status
    assert response.status_code == 200, f"Unexpected status: {response.status_code}, body: {response.text}"

    data = response.json()

    # Check validation results
    assert data["validation"]["exists"] is True
    assert data["validation"]["not_empty"] is True
    assert data["validation"]["page_count"] > 0