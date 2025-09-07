import re

def extract_name(text):
    """
    Extracts the candidate's name from text.
    Looks for the first line that:
      - Contains only letters and spaces
      - Has 2-4 words (typical name length)
    """
    lines = text.splitlines()
    for line in lines:
        clean_line = line.strip()
        if not clean_line:
            continue
        # check if line contains mostly letters
        if all(c.isalpha() or c.isspace() for c in clean_line):
            # only consider lines with 2-4 words as names
            if 2 <= len(clean_line.split()) <= 4:
                return clean_line
    return "Name not found"

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Email not found"

def extract_phone(text):
    match = re.search(r'\+?\d[\d\s\-]{7,}\d', text)
    return match.group(0) if match else "Phone not found"

def extract_education(text):
    edu_lines = []
    for line in text.splitlines():
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in ['university', 'college', 'master', 'bachelor']):
            clean_line = line.strip()
            if clean_line not in edu_lines:
                edu_lines.append(clean_line)
    return edu_lines if edu_lines else ["Education not found"]

def extract_experience(text):
    exp_lines = []
    skip_keywords = ['internship & experience', 'education']
    for line in text.splitlines():
        line_lower = line.lower()
        if any(job_keyword in line_lower for job_keyword in ['intern', 'engineer', 'developer', 'software']):
            clean_line = line.strip()
            if clean_line not in exp_lines:
                exp_lines.append(clean_line)
        elif any(skip in line_lower for skip in skip_keywords):
            continue
    return exp_lines if exp_lines else ["Experience not found"]

def extract_info(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "education": extract_education(text),
        "experience": extract_experience(text),
    }

if __name__ == "__main__":
    sample_text = "Paste your extracted text here for testing"
    info = extract_info(sample_text)
    print(info)
