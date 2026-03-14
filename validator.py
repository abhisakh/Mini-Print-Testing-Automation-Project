import os
from pypdf import PdfReader

def file_exists(file_path):
    return os.path.exists(file_path)

def file_not_empty(file_path):
    return os.path.getsize(file_path) > 0

def get_page_count(file_path):
    reader = PdfReader(file_path)
    return len(reader.pages)
