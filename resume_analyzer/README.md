# Resume Analyzer

## Overview
Resume Analyzer is a Python project designed to extract and structure information from resumes in PDF and DOCX formats. It extracts key details like name, email, phone number, education, and work experience, and saves them into a CSV file for easy analysis.

## Features
- Extract text from `.docx` and `.pdf` resumes.
- Parse structured information including:
  - Name
  - Email
  - Phone
  - Education
  - Experience
- Save extracted data into a CSV file.
- Works with multiple resumes in a folder.

## Project Structure
resume_analyzer/
│
├── resumes/ # Sample resumes
├── extractor/ # Extraction modules
│ ├── init.py
│ ├── pdf_extractor.py
│ ├── docx_extractor.py
│ └── info_extractor.py
├── api/ # API/main script
│ ├── init.py
│ └── main.py
├── data/
│ └── skills.txt # Skills reference file
├── requirements.txt
└── README.md

bash
Copy code

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd resume_analyzer
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate    # macOS/Linux
# OR
venv\Scripts\activate       # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the main script to extract information from resumes:

bash
Copy code
python -m api.main
Place your resumes in the resumes/ folder.

The extracted CSV will be saved as resumes_data.csv in the project root.

Dependencies
pdfminer.six==20250506

python-docx==1.2.0

lxml==6.0.1

cryptography==45.0.7

cffi==1.17.1

pycparser==2.22

charset-normalizer==3.4.3

typing_extensions==4.15.0

How it works
api/main.py scans the resumes/ folder for PDF and DOCX files.

For each resume:

Extract text using extract_text_from_docx or extract_text_from_pdf.

Parse structured information using extract_info.

All extracted data is written into resumes_data.csv.

Author
Rajkumar Rathlavath