# extractor/pdf_extractor.py

from pathlib import Path
import sys
import pdfminer.high_level

def extract_text_from_pdf(file_path: str) -> str:
    """
    Reads a PDF file and returns its text as a string.
    """
    try:
        text = pdfminer.high_level.extract_text(file_path)
        return text or ""
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

if __name__ == "__main__":
    # Check command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python extractor/pdf_extractor.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = Path(sys.argv[1]).expanduser().resolve()
    if not pdf_path.exists():
        print(f"File not found: {pdf_path}")
        sys.exit(1)

    extracted_text = extract_text_from_pdf(str(pdf_path))
    print("----- PDF Text Preview -----")
    print(extracted_text[:500])  # show first 500 chars
