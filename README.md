Resume Analyzer

Resume Analyzer is a web application that allows users to upload resumes (PDF or DOCX) and automatically extracts key information like name, email, phone, education, and experience. It’s built using FastAPI for the backend and supports a simple browser interface.

Features

Upload resumes in PDF or DOCX format.

Extracts key information: name, email, phone, education, experience.

View results instantly in the browser.

Simple, clean frontend with CSS styling.

Tech Stack

Backend: FastAPI

Frontend: HTML, CSS, JavaScript

Resume Parsing: Python libraries for DOCX/PDF extraction

Installation
# Clone the repository
git clone <your-repo-url>

# Navigate into project
cd resume_analyzer

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn api.main:app --reload --port 8001

Usage

Open browser at http://127.0.0.1:8001

Upload a PDF or DOCX resume

View extracted information on the page

Folder Structure
resume_analyzer/
├─ api/
│  ├─ main.py
│  ├─ templates/
│  └─ static/
├─ extractor/
│  ├─ pdf_extractor.py
│  ├─ docx_extractor.py
│  └─ info_extractor.py
├─ resumes/
├─ data/
├─ venv/
└─ README.md
