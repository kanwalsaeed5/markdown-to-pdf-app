import markdown
import pdfkit
import os

def markdown_to_html(markdown_text):
    """Convert Markdown text to HTML."""
    return markdown.markdown(markdown_text)

def html_to_pdf(html_text, output_path):
    """Convert HTML to PDF using pdfkit."""
    try:
        options = {
            'enable-local-file-access': None  # Needed for CSS
        }
        pdfkit.from_string(html_text, output_path, options=options)
        return True
    except Exception as e:
        print("Error generating PDF:", e)
        return False

def convert_markdown_file(input_path, output_path):
    """Convert a Markdown file to a formatted PDF."""
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Markdown file not found: {input_path}")

    with open(input_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    html_text = markdown_to_html(markdown_text)
    success = html_to_pdf(html_text, output_path)

    return success
