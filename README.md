# Resume Parser

A **Resume Parser** is a tool used to extract meaningful information from resumes (typically in formats like PDF, DOC, DOCX). The goal is to automatically retrieve important details such as name, contact information, education, competencies, and more, from a variety of resume formats. This parser can assist recruiters by automating the process of parsing and analyzing resumes, helping them quickly identify the best-fit candidates.

## Project Overview

This project demonstrates how to extract key information from resumes and save it in a structured format (JSON). It supports multiple file formats, including PDFs and DOCX files. The project makes use of libraries such as `PDFminer`, `doc2text`, `spaCy`, and `pandas` to extract relevant data points from resumes.

## Files

- **`parse_resume_to_json.py`**: The main script that parses the resume and extracts key details such as name, phone numbers, emails, competencies, and education.
- **`Bold-Boaz-Resume.docx`**: A sample DOCX resume file for testing the parser.
- **`London-Resume-Template-Professional.pdf`**: A sample PDF resume file for testing the parser.
- **`resume_parser.py`**: A Python file that handles the extraction process for various resume data points.
- **`index.html`**: A web interface that allows users to upload resumes for parsing.
- **`script.js`**: The JavaScript file supporting the web interface.
- **`style.css`**: The CSS file for styling the web interface.
- **`notification.mp3`**: A notification sound for indicating when the parsing is completed.

## Features

1. **Text Extraction**:
   - **PDF**: Extracts text from PDF files using `PDFminer`.
   - **DOC/DOCX**: Extracts text from DOC and DOCX files using `doc2text`.

2. **Name Extraction**:
   - Retrieves the name from resumes using rule-based matching with `spaCy`.

3. **Phone Number Extraction**:
   - Extracts phone numbers using regular expressions.

4. **Email Extraction**:
   - Extracts emails using regex-based methods.

5. **Competencies Extraction**:
   - Extracts and categorizes skills and competencies listed in the resume.

6. **Education Extraction**:
   - Retrieves educational qualifications from the resume using tokenization and named entity recognition.

7. **Structured Output**:
   - The extracted information is saved into a structured **JSON** format.
