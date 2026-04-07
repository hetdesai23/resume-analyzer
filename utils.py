import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🔥 Generic words to ignore
GENERIC_WORDS = set([
    "work", "team", "skills", "ability", "knowledge", "responsible",
    "good", "strong", "understanding", "experience", "working",
    "technical", "management", "development", "tasks"
])

# 🔥 Skill groups (domain-agnostic)
SKILL_GROUPS = {
    "Programming": ["python", "java", "c++", "c", "r"],
    "Web Development": ["html", "css", "javascript", "frontend", "backend"],
    "Frameworks": ["django", "flask", "react", "fastapi", "angular"],
    "Data & AI": ["machine learning", "deep learning", "nlp", "pandas", "numpy"],
    "Databases": ["sql", "mysql", "postgresql", "mongodb"],
    "Tools": ["git", "docker", "aws", "excel"],
    "Finance": ["valuation", "financial modeling", "investment"],
    "Marketing": ["seo", "branding", "ads", "content marketing"]
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    return text


# 🔥 Simple tokenizer (NO NLTK)
def extract_keywords(text):
    words = text.split()
    words = [w for w in words if w not in GENERIC_WORDS and len(w) > 2]
    return set(words)


def extract_skills_by_group(text):
    found = {}
    for group, skills in SKILL_GROUPS.items():
        matched = [s for s in skills if s in text]
        if matched:
            found[group] = matched
    return found


def semantic_score(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    return cosine_similarity(vectors[0:1], vectors[1:2])[0][0]


def analyze_resume(resume_text, job_description):
    resume_text = clean_text(resume_text)
    job_description = clean_text(job_description)

    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(job_description)

    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords - resume_keywords

    # Remove generic words
    missing = [w for w in missing if w not in GENERIC_WORDS]

    keyword_score = len(matched) / len(jd_keywords) if len(jd_keywords) > 0 else 0
    semantic = semantic_score(resume_text, job_description)

    final_score = (0.6 * keyword_score + 0.4 * semantic) * 100

    # 🔥 Skill grouping
    resume_groups = extract_skills_by_group(resume_text)
    jd_groups = extract_skills_by_group(job_description)

    strong = []
    missing_groups = []

    for group in jd_groups:
        if group in resume_groups:
            strong.append(group)
        else:
            missing_groups.append(group)

    # 🔥 Smart suggestions
    suggestions = []

    for group in missing_groups:
        if group == "Frameworks":
            suggestions.append("Build a project using Django or Flask")
        elif group == "Databases":
            suggestions.append("Add database experience like MySQL or MongoDB")
        elif group == "Tools":
            suggestions.append("Use Git & upload projects on GitHub")
        elif group == "Web Development":
            suggestions.append("Learn basic frontend (HTML, CSS, JS)")
        elif group == "Data & AI":
            suggestions.append("Create ML/NLP projects using Python")
        else:
            suggestions.append(f"Improve skills in {group}")

    return {
        "score": round(final_score, 2),
        "strong": strong,
        "missing_groups": missing_groups,
        "suggestions": suggestions
    }
def generate_resume_improvements(missing_groups):
    improvements = []

    for group in missing_groups:
        if group == "Frameworks":
            improvements.append(
                "Built scalable web applications using Django/Flask, implementing REST APIs and backend logic."
            )
        elif group == "Databases":
            improvements.append(
                "Worked with databases like MySQL/PostgreSQL to design and manage structured data efficiently."
            )
        elif group == "Tools":
            improvements.append(
                "Used Git for version control and collaborated on projects via GitHub."
            )
        elif group == "Web Development":
            improvements.append(
                "Developed responsive user interfaces using HTML, CSS, and JavaScript."
            )
        elif group == "Data & AI":
            improvements.append(
                "Developed machine learning models using Python libraries like Pandas and Scikit-learn."
            )
        elif group == "Programming":
            improvements.append(
                "Strong programming skills with problem-solving using languages like Python/Java."
            )
        else:
            improvements.append(f"Demonstrated practical experience in {group} through projects or internships.")

    return improvements