# 🔍 Resume vs Job Description Matcher

A simple but powerful Python tool to compare your resume with a job description and get an instant skill match report. Designed for students, job seekers, and anyone preparing for tech interviews!

---

## 🚀 Features

- ✅ Extracts text from resume PDF
- 🧠 Uses NLP to find important keywords
- 📊 Calculates match percentage
- 🔎 Shows matched and missing skills
- ⚡ Beginner-friendly & fast to run

---

## 🛠️ Technologies Used

- Python 3.x  
- [PyPDF2](https://pypi.org/project/PyPDF2/) – for reading PDF resumes  
- [NLTK](https://www.nltk.org/) – for natural language processing (stopword removal, tokenization)

---

## 📥 Installation

```bash
# Clone this repository
git clone https://github.com/smarty-vicky/resume-matcher.git
cd resume-matcher

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install PyPDF2 nltk
