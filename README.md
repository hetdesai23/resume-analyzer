AI Resume Analyzer

A resume analysis tool that evaluates how well a resume matches a given job description and provides practical suggestions for improvement. The project is designed to be simple, domain-agnostic, and useful for students and job seekers preparing for internships or entry-level roles.

Overview

The application allows users to upload a resume in PDF format and paste a job description. It analyzes both inputs and generates meaningful insights to help improve the resume.

The output includes:

- A match score indicating overall alignment  
- Identification of strong areas in the resume  
- Detection of missing or underrepresented skill categories  
- Actionable suggestions to improve the resume  
- Ready-to-use lines that can be added directly to the resume  

How It Works

The system follows a simple pipeline:

1. Extracts text from the uploaded PDF resume  
2. Cleans and normalizes the text data  
3. Compares the resume with the job description using:
   - Keyword overlap  
   - TF-IDF vectorization  
   - Cosine similarity  
4. Groups skills into broader categories to support multiple domains  
5. Generates suggestions and improvement statements based on missing areas  

Features

- Resume-to-job matching with a clear score  
- Domain-independent skill grouping  
- Identification of strengths and gaps  
- Actionable recommendations instead of generic feedback  
- Resume improvement lines that can be directly reused  
- Simple and interactive interface built with Streamlit  

Tech Stack

- Python  
- Streamlit  
- Scikit-learn  
- PyPDF2  

Usage

1. Upload a resume in PDF format  
2. Paste the job description  
3. View the analysis, including score, strengths, missing areas, and suggestions  

Example Output

- Match Score: Indicates how closely the resume aligns with the job  
- Strong Areas: Skill categories already well represented  
- Missing Areas: Important skill groups not clearly present  
- Suggestions: Specific steps to improve the resume  
- Improvement Lines: Pre-written statements that can be added to the resume  

Demo
https://resume-analyzer-xvzanqbykdiktjimzuugis.streamlit.app

Use Cases

- Students applying for internships  
- Fresh graduates preparing their resumes  
- Anyone looking to tailor their resume for a specific job role  

Future Scope

- Resume editing and download functionality  
- Support for multiple resume comparisons  
- Integration with more advanced NLP models  
- Improved scoring and feedback system  

---

## Author

Het Desai
