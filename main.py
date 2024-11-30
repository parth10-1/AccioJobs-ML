import os
from dotenv import load_dotenv
from baml_client import b
from baml_client.types import Resume
import app.database as db
import app.pdfread as pdfread
import json


def load_environment_variables():
    load_dotenv()
    return os.getenv("CONN_URL")

def get_job_data(conn_url, id):
    #Job Data
    return db.get_job_data(conn_url)

def extract_text_from_pdf():
    #Extract Text from PDF
    return pdfread.extract_text_from_pdf()

def extract_resume(resume_text, job_description):
    #Extract Resume
    baml_object = b.ExtractResume(resume_text, job_description).model_dump_json()
    #assert isinstance(baml_object, Resume)
    #json_object = json.dumps(baml_object, indent=4)
    return baml_object

def main():
    conn_url = load_environment_variables()
    job_description = "Data Analyst"
    resume_text = """Vaibhav Gupta
vbv@boundaryml.com
Experience:
- Founder at BoundaryML
- CV Engineer at Google
- CV Engineer at Microsoft
Skills:
- Rust
- C++"""
    resume = extract_resume(resume_text, job_description)
    
    print(resume)

if __name__ == "__main__":
    main()
