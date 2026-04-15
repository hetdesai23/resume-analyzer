import streamlit as st
import PyPDF2
from utils import analyze_resume, generate_resume_improvements

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("🚀 Resume Analyzer")
st.caption("Analyse how well your resume matches a job description.")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("📌 Paste Job Description")


def extract_pdf_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


if uploaded_file and job_description:

    resume_text = extract_pdf_text(uploaded_file)
    result = analyze_resume(resume_text, job_description)
    improvements = generate_resume_improvements(result["missing_groups"])

    score = result["score"]

    # SCORE CARD
    st.markdown("## 📊 Resume Strength")

    st.progress(score / 100)

    if score > 70:
        st.success(f"{score}% — Strong profile 🚀")
    elif score > 40:
        st.warning(f"{score}% — متوسط (Needs improvement) ⚠️")
    else:
        st.error(f"{score}% — Needs improvement — you're on the right track ⚠️")

    # STRONG AREAS
    st.markdown("## 🟢 Where You’re Strong")
    if result["strong"]:
        for s in result["strong"]:
            st.write(f"✔ {s}")
    else:
        st.write("No strong areas detected")

    # MISSING
    st.markdown("## 🔴 What You're Missing")
    if result["missing_groups"]:
        for m in result["missing_groups"]:
            st.write(f"➕ {m}")
    else:
        st.write("No major gaps")

    # ACTION PLAN
    st.markdown("## 💡 Action Plan")
    for i, sug in enumerate(result["suggestions"], 1):
        st.write(f"{i}. {sug}")

    # RESUME IMPROVEMENT 
    st.markdown("## ✍️ Improve Your Resume (Use these lines)")

    for line in improvements:
        st.code(line)

    # SUMMARY
    st.markdown("## 📌 Final Summary")
    st.write(f"✔ Match Score: {score}%")
    st.write(f"✔ Strong Areas: {len(result['strong'])}")
    st.write(f"✔ Missing Areas: {len(result['missing_groups'])}")

else:
    st.info("Upload resume and paste job description to begin")