from django.core.files.uploadedfile import UploadedFile
import pymupdf
import ollama
import json

def read_upload_file(file_object : UploadedFile , file_extension : str) -> str:
    with pymupdf.open(stream=file_object.read(),filetype=file_extension) as document:
        text = ""
        for page_number in range(len(document)):
            page = document.load_page(page_number)
            text += page.get_text()

    return text

def extract_resume_information(file_content : str):
    prompt_data = """
        You are an AI bot designed to act as a professional for parsing resumes. You are given a resume  and your job is to
        extract the following information from the resume:

        1. applicant_name: ""
        2. highest_level_of_education: ""
        3. area_of_study: ""
        4. institution:""
        5. introduction : ""
        6. skills: string []
        7. english_proficiency_level: ""
        8. experiences: [{"employer_name":"", role:"",  duration:""}]

        Give the extracted info in JSON format only.
        Note: if the info is not present, leave the field blank.
    """
    
    response = ollama.chat(model="llama3.2:3b",messages=[{
        'role': 'assistant',
        'content': prompt_data,
    },{
        'role': 'user',
        'content': file_content
    }],format='json')
    
    # convert the response to a dictionary
    response = json.loads(response['message']['content'])
    
    print(response)
    
    return response