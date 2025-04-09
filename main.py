from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import markdown
from weasyprint import HTML
import spacy
import os
import tempfile
import re

app = FastAPI()
nlp = spacy.load("en_core_web_sm")

# You can expand this list based on misclassified terms
EXCLUDED_ENTITIES = ["ChatFormatter", "Convert"]

def clean_text(text: str) -> str:
    # Remove markdown headers (##, ###, etc.) and clean unnecessary characters
    text = re.sub(r'##+\s*', '', text)
    # Add any other specific text preprocessing steps you may need
    return text

@app.post("/convert/")
async def convert_markdown_to_pdf(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text = contents.decode("utf-8")

        # --- Step 1: Clean and preprocess the text ---
        cleaned_text = clean_text(text)

        # --- Step 2: Convert Markdown to HTML ---
        html_body = markdown.markdown(cleaned_text)

        # --- Step 3: Export to PDF using a temporary file ---
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_pdf:
            output_pdf_path = tmp_pdf.name
            HTML(string=html_body).write_pdf(output_pdf_path)

        return FileResponse(path=output_pdf_path, filename="output.pdf", media_type="application/pdf")

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}