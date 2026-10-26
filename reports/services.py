import os
from pathlib import Path
from io import BytesIO
import markdown
from pypdf import PdfReader
from google import genai
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def extract_text(uploaded_file):
    filename = uploaded_file.name.lower()

    if filename.endswith(".txt"):
        text = uploaded_file.read().decode(
            "utf-8", errors="replace"
        )

    elif filename.endswith(".pdf"):
        pdf = PdfReader(BytesIO(uploaded_file.read()))
        text = ""

        for page in pdf.pages:
            text += page.extract_text() or ""
            text += "\n"

    else:
        raise ValueError("Unsupported file format.")

    if not text.strip():
        raise ValueError(
            "No readable text found. Scanned PDFs need OCR."
        )

    return text


def explain_report(report_text):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not found in .env.")

    client = genai.Client(api_key=api_key)

    prompt = f"""
    Explain this medical report in simple language.

    Include:
    1. A short summary.
    2. Explanation of medical terms.
    3. Important values explicitly present in the report.
    4. Questions the patient can ask their doctor.

    Do not diagnose diseases or recommend medicines.
    Do not invent missing values or reference ranges.
    Clearly mention when information is unclear.

    Medical report:
    {report_text}
    """

    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response.")

    return markdown.markdown(
    response.text,
    extensions=["extra"]
    )