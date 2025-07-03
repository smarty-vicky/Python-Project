# resume_matcher.py

import PyPDF2
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already available
nltk.download('stopwords')

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a given PDF file.

    Parameters:
    - pdf_path (str): The path to the resume PDF file.

    Returns:
    - str: Extracted plain text from the PDF.
    """
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except FileNotFoundError:
        print("❌ PDF file not found. Please check the path.")
    return text


def extract_keywords(text):
    """
    Cleans and extracts keywords from raw text.

    Parameters:
    - text (str): Input text.

    Returns:
    - set: Set of meaningful keywords.
    """
    stop_words = set(stopwords.words('english'))
    words = text.lower().split()
    keywords = [word for word in words if word.isalpha() and word not in stop_words]
    return set(keywords)


def match_resume_with_jd(resume_path, jd_text):
    """
    Compares resume keywords to job description keywords
    and prints match statistics.

    Parameters:
    - resume_path (str): File path to the resume PDF.
    - jd_text (str): Job description input from user.
    """
    resume_text = extract_text_from_pdf(resume_path)
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    matched = resume_keywords.intersection(jd_keywords)
    missing = jd_keywords - resume_keywords
    match_percent = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0

    print("\n🔍 Resume Matching Results 🔍")
    print(f"✅ Match Percentage: {match_percent:.2f}%")
    print(f"\n✅ Matched Skills:\n{', '.join(matched) if matched else 'None'}")
    print(f"\n❌ Missing Skills:\n{', '.join(missing) if missing else 'None'}")


if __name__ == "__main__":
    print("📄 Resume vs Job Description Matcher 🔎")
    resume_path = input("Enter your resume PDF path: ").strip()
    jd_input = input("Paste the Job Description here:\n").strip()
    match_resume_with_jd(resume_path, jd_input)
