import streamlit as st
import PyPDF2
import docx
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import os
nltk_data_path = os.path.join(os.path.expanduser('~'), 'nltk_data')
nltk.download('stopwords', download_dir=nltk_data_path)
nltk.data.path.append(nltk_data_path)


# ---------- Helper Functions ----------

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    tokens = text.split()
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(similarity * 100, 2)

# ---------- Streamlit UI ----------

st.title("📄 Resume Analyzer AI")
st.write("Upload your resume and paste a job description to get a match score.")

uploaded_file = st.file_uploader("Upload your Resume (.pdf or .docx)", type=["pdf", "docx"])
job_description = st.text_area("Paste Job Description Here")

if st.button("Analyze"):
    if uploaded_file is not None and job_description.strip() != "":
        if uploaded_file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            resume_text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file format")
            resume_text = ""

        resume_clean = clean_text(resume_text)
        jd_clean = clean_text(job_description)

        score = calculate_similarity(resume_clean, jd_clean)

        st.success(f"✅ Resume Match Score: {score}%")
        if score >= 70:
            st.info("Great! Your resume is a good match.")
        else:
            st.warning("You may want to tweak your resume for better alignment.")
    else:
        st.error("Please upload a resume and paste a job description.")
