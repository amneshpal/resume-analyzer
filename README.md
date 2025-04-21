# Resume Analyzer AI

This is a **Resume Analyzer AI** app built with **Streamlit**, **Python**, and **scikit-learn**. The app helps you compare a job description (JD) with your resume to determine how well your resume matches the job description. The result is presented as a match score (percentage), giving feedback on how aligned your resume is with the job description.

## Features

- **Upload Resume**: Upload your resume in PDF or DOCX format.
- **Job Description**: Paste the job description text.
- **Match Score**: Get a match score (from 0 to 100%) based on text similarity.
- **Feedback**: Receive feedback on how to improve your resume for a better match.

## Tech Stack

- **Backend**: Python
- **Libraries/Frameworks**:
  - **Streamlit**: For building the interactive web app.
  - **PyPDF2**: To extract text from PDF files.
  - **python-docx**: To extract text from DOCX files.
  - **nltk**: For natural language processing (removing stop words).
  - **scikit-learn**: To calculate the similarity score using TF-IDF vectorization and cosine similarity.
- **Deployment**: Streamlit Cloud for hosting the app.

## Setup Instructions

## Live Demo

You can try the **Resume Analyzer AI** app here:

[Resume Analyzer AI - Live Demo](https://resume-analyzer-gakq2yq5uzkwaqv7exsjpj.streamlit.app/)
### 1. Clone the Repository

```bash
git clone https://github.com/amneshpal/resume-analyzer.git
cd resume-analyzer



