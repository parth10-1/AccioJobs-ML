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
    baml_object = b.ExtractResume(resume_text, job_description).model_dump_json()
    return baml_object

def main():
    conn_url = load_environment_variables()
    job_description = get_job_data(conn_url)
    resume_text = extract_text_from_pdf()
    resume = extract_resume(resume_text, job_description)
    
    print(resume)

if __name__ == "__main__":
    main()