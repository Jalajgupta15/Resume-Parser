from flask import Flask, request, jsonify
from pdfminer.high_level import extract_text as extract_text_from_pdf
import docx2txt
import spacy
import pandas as pd
from nltk.corpus import stopwords
import re
import os

app = Flask(__name__)

# Load pre-trained model
nlp = spacy.load('en_core_web_sm')

# General stop words
STOPWORDS = set(stopwords.words('english'))

# Education Degrees
EDUCATION = [
    'BE', 'B.E.', 'B.E', 'BS', 'B.S',
    'ME', 'M.E', 'M.E.', 'MS', 'M.S',
    'BTECH', 'B.Tech', 'M.Tech', 'MTECH',
    'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
]

def extract_text_from_doc(doc_path):
    return docx2txt.process(doc_path)

def extract_skills(resume_text):
    nlp_text = nlp(resume_text)
    tokens = [token.text for token in nlp_text if not token.is_stop]
    data = pd.read_csv("skills.csv")
    skills = list(data.columns.values)
    skillset = []
    for token in tokens:
        if token.lower() in skills:
            skillset.append(token)
    for chunk in nlp_text.noun_chunks:
        chunk = chunk.text.lower().strip()
        if chunk in skills:
            skillset.append(chunk)
    return [i.capitalize() for i in set([i.lower() for i in skillset])]

def extract_education(resume_text):
    nlp_text = nlp(resume_text)
    nlp_text = [sent.string.strip() for sent in nlp_text.sents]
    edu = {}
    for index, text in enumerate(nlp_text):
        for tex in text.split():
            tex = re.sub(r'[?|$|.|!|,]', r'', tex)
            if tex.upper() in EDUCATION and tex not in STOPWORDS:
                edu[tex] = text + nlp_text[index + 1]
    education = []
    for key in edu.keys():
        year = re.search(re.compile(r'(((20|19)(\\d{2})))'), edu[key])
        if year:
            education.append((key, ''.join(year[0])))
        else:
            education.append(key)
    return education

def extract_experience(resume_text):
    experience = []
    lines = resume_text.split('\n')
    for line in lines:
        if re.search(r'\bexperience\b', line, re.IGNORECASE):
            exp = {}
            exp['title'] = line.strip()
            exp['details'] = []
            while line.strip():
                exp['details'].append(line.strip())
                line = next(lines, None)
            experience.append(exp)
    return experience

def calculate_ats_score(skills, education, experience):
    score = 0
    if skills:
        score += len(skills) * 10
    if education:
        score += len(education) * 15
    if experience:
        score += len(experience) * 20
    return score

@app.route('/parse_resume', methods=['POST'])
def parse_resume():
    file = request.files['file']
    if file.filename.endswith('.pdf'):
        resume_text = extract_text_from_pdf(file)
    elif file.filename.endswith('.docx'):
        resume_text = extract_text_from_doc(file)
    else:
        return jsonify({"error": "File format not supported"}), 400
    
    skills = extract_skills(resume_text)
    education = extract_education(resume_text)
    experience = extract_experience(resume_text)
    ats_score = calculate_ats_score(skills, education, experience)
    
    return jsonify({"skills": skills, "education": education, "experience": experience, "ats_score": ats_score})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', 5000))
