from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.nlp_processor import preprocess_text, extract_skills
from utils.semantic_matcher import calculate_similarity
import os

from utils.resume_parser import extract_text_from_pdf

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return {"message": "Backend Running"}

@app.route('/upload', methods=['POST'])
def upload_resume():

    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['resume']

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(file_path)

    extracted_text = extract_text_from_pdf(file_path)

    tokens = preprocess_text(extracted_text)

    skills = extract_skills(tokens)
    job_description = request.form.get('job_description')
    match_score = calculate_similarity(
    extracted_text,
    job_description
    )
    return jsonify({
    "filename": file.filename,
    "skills": skills,
    "resume_text": extracted_text,
    "match_score": match_score
    })

if __name__ == '__main__':
    app.run(debug=True)