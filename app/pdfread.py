import fitz

def extract_text_from_pdf():
    my_path = 'PATH_TO_PDF'
    doc = fitz.open(my_path)
    resume_text = ""
    for page in doc:
        text = page.get_text()
        resume_text += text
    return resume_text
