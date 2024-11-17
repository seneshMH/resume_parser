from django.shortcuts import render
from django.http import HttpRequest,JsonResponse
from django.core.files.uploadedfile import UploadedFile
from django.core.exceptions import ValidationError

from .validators import validate_file_extension, validate_file_size
from .utils import read_upload_file , extract_resume_information

# Create your views here.
def home(request : HttpRequest):
    return render(request, "index.html")

def upload_resume(request : HttpRequest):
    if request.method == "POST" and request.FILES.get("file"):
        file : UploadedFile = request.FILES["file"]
        try:
            ext:str = validate_file_extension(file)
            validate_file_size(file)
            file_content = read_upload_file(file,ext)
            response = extract_resume_information(file_content)
            
            return JsonResponse({"message": "File uploaded successfully" , "data" : response}, status=200)
        except ValidationError as e:
              return JsonResponse({"error": e.message}, status=400)
    return JsonResponse({"error": "No file uploaded"}, status=400)