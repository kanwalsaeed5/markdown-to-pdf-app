# For future extensions like sanitizing HTML or custom styling

def apply_custom_css(html):
    """Apply basic CSS styles to HTML content."""
    style = """
    <style>
        body { font-family: 'Arial'; padding: 20px; }
        h1, h2, h3 { color: #2c3e50; }
        pre { background-color: #f4f4f4; padding: 10px; }
        code { color: #e74c3c; }
    </style>
    """
    return style + html
