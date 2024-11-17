from parser.utils import read_upload_file
from .conftest import FILE_CONTENT

def test_read_upload_pdf_file(generate_pdf_file):
    with open(generate_pdf_file, "rb") as file_object:
        test_result = read_upload_file(file_object,"pdf")
        assert test_result == FILE_CONTENT+"\n"

def test_read_upload_doc_file(generate_doc_file):
    with open(generate_doc_file, "rb") as file_object:
        test_result = read_upload_file(file_object,"docx")
        assert test_result == FILE_CONTENT+"\n"