import os
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from extractor.docx_extractor import extract_text_from_docx
from extractor.pdf_extractor import extract_text_from_pdf
from extractor.info_extractor import extract_info

app = FastAPI(title="Resume Analyzer API")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESUME_FOLDER = os.path.join(BASE_DIR, "resumes")
os.makedirs(RESUME_FOLDER, exist_ok=True)

# Mount static folder
app.mount("/static", StaticFiles(directory="api/static"), name="static")

# Templates
templates = Jinja2Templates(directory="api/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/analyze/")
async def analyze_resume(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(RESUME_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        if file.filename.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        elif file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        else:
            return {"error": "Unsupported file type"}

        info = extract_info(text)
        info["education"] = " | ".join(info.get("education", []))
        info["experience"] = " | ".join(info.get("experience", []))

        os.remove(file_path)
        return info
    except Exception as e:
        return {"error": str(e)}
