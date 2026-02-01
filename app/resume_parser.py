import pdfplumber
from docx import Document


def parse_resume(file_path: str) -> str:
    text = ""

    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        text = " ".join(p.text for p in doc.paragraphs)

    return text.lower()
