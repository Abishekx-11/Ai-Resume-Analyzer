
import PyPDF2
from flask import Flask, render_template, request,  url_for
from google import genai
from google.genai import types
from PyPDF2 import PdfReader
from configure import API_KEY
import os 


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
    
# Helper Functions 
#------------------------------------------------------------------------------------
def extract_text(filepath):
    pdf_text = PyPDF2.PdfReader(filepath)
    text = ""
    for page in pdf_text.pages:
        text = text + page.extract_text()
    return text
#------------------------------------------------------------------------------------

def analyze_with_ai(pdf_text):
    client = genai.Client(api_key=API_KEY)
    prompt = f"""
        You are an expert HR recruiter and resume analyst. Analyze the following resume and provide:
    
    1. Overall Summary (2-3 sentences)
    2. Key Strengths (list 4-5 points)
    3. Areas for Improvement (list 3-4 points)
    4. Skills Identified (categorize: technical, soft skills)
    5. ATS (Applicant Tracking System) Score out of 100
    6. Recommendations for improvement
    
    Resume Content:
    {pdf_text}
    
    Provide a detailed, professional analysis in a well-structured format.
    """
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents= prompt,
        config= types.GenerateContentConfig(
            temperature= 0.2
        )
    )

    return response.text
#------------------------------------------------------------------------------------



@app.route("/")
def indeX():
    return render_template("index.html")


@app.route('/analyze' , methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return "No files uploaded", 400
    
    file = request.files['resume']

    if file.filename == '':
        return "No file selected", 400
    
    filename = file.filename

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    pdf_text= extract_text(filepath)

    ai_analysis = analyze_with_ai(pdf_text)

    os.remove(filepath)

    return render_template("result.html", analysis = ai_analysis)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)    #using this to deploy it in render
    # app.run(debug=True)






