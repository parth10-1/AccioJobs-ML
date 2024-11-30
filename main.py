import os
from dotenv import load_dotenv
from baml_client import b
from baml_client.types import Resume
import app.database as db
import app.pdfread as pdfread


def load_environment_variables():
    load_dotenv()
    return os.getenv("CONN_URL")

def get_job_data(conn_url):
    #Job Data
    return db.get_job_data(conn_url)

def extract_text_from_pdf():
    #Extract Text from PDF
    return pdfread.extract_text_from_pdf()

def extract_resume(resume_text, job_description):
    #Extract Resume
    return b.ExtractResume(resume_text, job_description)

def main():
    conn_url = load_environment_variables()
    job_description = get_job_data(conn_url)
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
    assert isinstance(resume, Resume)
    print(resume)

if __name__ == "__main__":
    main()