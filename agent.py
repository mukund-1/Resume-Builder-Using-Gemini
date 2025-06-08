import os
import google.generativeai as genai
from html_to_pdf import create_pdf_from_resume_text


def resume_agent(user_data):
    # Step 1: Ask Gemini to improve content
    resume_prompt = f"""Act like a professional resume writer.

    Generate a resume based on the following information:
    
    Name: {user_data['name']}
    Email: {user_data['email']}
    Summary: {user_data['summary']}
    Skills: {', '.join(user_data['skills'])}
    education: {user_data['education']}
    Experience: {user_data['experience']}
    
    Make sure the resume has sections:

    Header (name, contact)

    Summary

    Education

    Experience

    Skills

    Keep it professional and concise.
    """
    improved_resume = generate_with_gemini(resume_prompt)
    print(f"Improved Resume: {improved_resume}")
    # Step 2: Convert response to PDF
    pdf_bytes = create_pdf_from_resume_text(improved_resume)

    return pdf_bytes

# Set your API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyD44odvaci8mt3ElvyepB5ux49ce-tsJZs"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def generate_with_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-1.5-flash")  # or "gemini-1.5-pro"
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    prompt = "generate a mock resume for a software engineer with skills in Python, JavaScript, and machine learning"
    response = generate_with_gemini(prompt)
    print(f"Response from Gemini: {response}")
