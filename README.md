# AI Medical Report Explainer 🩺

An AI-powered web application that helps users understand medical reports in simple, easy-to-understand language.

## 📌 About the Project

Medical reports often contain complex medical terms and test results that can be difficult for non-medical users to understand. This project aims to simplify medical information by analyzing uploaded reports and generating clear explanations.

Users can upload a medical report and receive a simplified explanation of its contents, helping them better understand the information in their reports.

## ✨ Features

- 📄 Upload medical reports in PDF format.
- 🤖 AI-powered analysis and explanation of medical information.
- 📝 Simplifies complex medical terminology into understandable language.
- 🔍 Helps users identify important findings mentioned in their reports.
- 🌐 Simple and user-friendly web interface.

## 🛠️ Technologies Used

- **Backend:** Python, Django
- **Frontend:**  Django Templates, HTML, CSS, JavaScript
- **AI Integration:** gemini API
- **Document Processing:** PDF text extraction

*Note: Update this list to match the technologies and libraries actually implemented in your project.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shruti-dev121/Medical_reporter_explainer.git
```

### 2. Navigate to the project directory

```bash
cd Medical_reporter_explainer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project directory and add your API key if required.

```env
OPENAI_API_KEY=your_api_key_here
```

Never upload your actual API key to GitHub.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

Open the local URL shown in the terminal, usually `http://127.0.0.1:8000/`.

## 🚀 Future Improvements

- Support for scanned PDFs using OCR.
- Display extracted medical values in a structured format.
- Highlight abnormal results when reference ranges are available.
- Add report history and downloadable summaries.
- Improve accessibility and mobile responsiveness.

## ⚠️ Medical Disclaimer

This application is intended for educational and informational purposes only. It does not provide medical diagnoses or replace professional medical advice. Users should consult a qualified healthcare professional for interpretation of their medical results and treatment decisions.

## 👩‍💻 Author

**Shruti**

GitHub: [shruti-dev121](https://github.com/shruti-dev121)

---

⭐ If you find this project useful, consider giving the repository a star.
