from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError
import os

VALID_EXTENSIONS = [".pdf", ".docx" , ".doc"]

def validate_file_extension(file_object: UploadedFile):
    ext : str = os.path.splitext(file_object.name)[1]
    if ext.lower() not in VALID_EXTENSIONS:
        raise ValidationError(f"Unsupported file extension {ext}")
    return ext.lower()

def validate_file_size(file_object: UploadedFile):
    MAX_UPLOAD_SIZE = 10 * 1024 * 1024
    if file_object.size > MAX_UPLOAD_SIZE:
        raise ValidationError(f"File size exceeds the limit of {MAX_UPLOAD_SIZE} bytes")