from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.nlp_processor import preprocess_text, extract_skills
from utils.semantic_matcher import calculate_similarity
from utils.ranking import calculate_final_score
from utils.entity_extractor import extract_entities
from utils.bias_detector import anonymize_resume 

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
    entities = extract_entities(extracted_text)
    anonymous_text, removed_items, fairness_score = anonymize_resume(
        extracted_text,
        entities
    )

    tokens = preprocess_text(extracted_text)

    skills = extract_skills(tokens)

    job_description = request.form.get('job_description')

    match_score = calculate_similarity(
        anonymous_text,
        job_description
    )
    skill_count = len(skills)

    final_score = calculate_final_score(
        match_score,
        skill_count
    )
    return jsonify({

    "filename": file.filename,

    "resume_text": extracted_text,

    "skills": skills,

    "match_score": match_score,

    "final_score": final_score,

    "entities": entities,
    "anonymous_resume": anonymous_text,
    "removed_items": removed_items,
    "fairness_score": fairness_score


    })

if __name__ == '__main__':
    app.run(debug=True)