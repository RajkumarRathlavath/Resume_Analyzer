from pathlib import Path
from docx import Document
import sys

def extract_text_from_docx(file_path: str) -> str:
    """
    Reads a DOCX file and returns its text as a string.
    """
    try:
        doc = Document(file_path)
        full_text = [para.text for para in doc.paragraphs]
        return "\n".join(full_text)
    except Exception as e:
        print(f"Error reading DOCX: {e}")
        return ""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python docx_extractor.py <path_to_docx>")
        sys.exit(1)

    docx_path = Path(sys.argv[1]).expanduser().resolve()
    if not docx_path.exists():
        print(f"File not found: {docx_path}")
        sys.exit(1)

    text = extract_text_from_docx(str(docx_path))
    print("----- DOCX Text Preview -----")
    print(text[:500])
