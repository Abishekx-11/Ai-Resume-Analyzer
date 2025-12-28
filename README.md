# AI Resume Analyzer 🤖📄

An AI-powered web application that analyzes resumes and provides instant feedback using Google's Gemini AI.

## Features ✨

- Upload PDF resumes
- AI-powered analysis using Google Gemini
- Get detailed feedback on:
  - Overall summary
  - Key strengths
  - Areas for improvement
  - Skills identification
  - ATS score out of 100
  - Recommendations

## Tech Stack 🛠️

- **Backend:** Flask (Python)
- **AI:** Google Gemini API
- **PDF Processing:** PyPDF2
- **Frontend:** HTML, CSS



## Project Structure 📁
```
ai-resume-analyzer/
│
├── app.py                 # Main Flask application
├── configure.py              # API key configuration (not in git)
├── requirements.txt       # Python dependencies
│
├── templates/
│   ├── index.html        # Home page with upload form
│   └── result.html       # Results display page
│
├── static/
│   └── style.css         # CSS styling
│
└── uploads/              # Temporary file storage (auto-deleted)
```

## ⚙️ API Key Setup

Create a file named `configure.py` in the project root directory:
```python
API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"
```



## Usage 🚀

1. **Run the application**
```bash
python app.py
```

3. **Upload resume**
- Click "Choose File"
- Select a PDF resume
- Click "Analyze Resume"
- View AI-generated analysis!

## Screenshots 📸

<img width="1573" height="823" alt="image" src="https://github.com/user-attachments/assets/aa4f0db8-ca39-46ac-a4cc-a46da05c0734" />

<img width="1868" height="865" alt="image" src="https://github.com/user-attachments/assets/c73809e3-2eb3-46b1-af97-28599389c5af" />



## Configuration ⚙️

- **Max file size:** 16MB
- **Accepted formats:** PDF only
- **AI Model:** Gemini 2.5 Flash

## License 📝

This project is open source and available under the [MIT License](LICENSE).
