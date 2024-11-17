from parser.validators import validate_file_extension , validate_file_size
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
import pytest

@pytest.mark.parametrize(
    "extension , is_exception_expected",
    [
        ("pdf" , False),
        ("docx" , False),
        ("doc" , False),
        ("txt" , True),
        ("ppt" , True),
        ("pptx" , True),
    ]
)
def test_validate_file_extension(extension , is_exception_expected):
    file = SimpleUploadedFile(f"test_file.{extension}" , b"Note")
    if is_exception_expected:
        with pytest.raises(ValidationError , match = f"Unsupported file extension .{extension}"):
            validate_file_extension(file)
    else:
        assert validate_file_extension(file)


@pytest.mark.parametrize(
    "file_size , is_exception_expected",
    [
        (10 * 1024 * 1024 , False),
        (10 * 1024 * 1024 + 1 , True),
        (10 * 1024 * 1024 - 1 , False),
    ]
)
def test_validate_file_size(file_size,is_exception_expected):
    file = SimpleUploadedFile(f"test_file.pdf" , b"Note")
    file.size = file_size
    if is_exception_expected:
        with pytest.raises(ValidationError , match = f"File size exceeds the limit of {10 * 1024 * 1024} bytes"):
            validate_file_size(file)
    else:
        assert not validate_file_size(file)
    pass