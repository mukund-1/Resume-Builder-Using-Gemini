
# 🧠 AI Resume Builder with Streamlit & MySQL

This project is a simple AI-powered Resume Builder that enables users to:

- Input their professional information
- Automatically generate a resume in PDF format using an LLM agent
- Save generated resumes to a MySQL database
- Retrieve and view saved resumes by ID
- Download resumes
- Optionally edit resumes manually after generation

---

## 🚀 Features

- ✅ AI-generated resume in PDF format
- ✅ Streamlit web interface
- ✅ Resume storage and retrieval using MySQL
- ✅ Inline PDF display and download
- ✅ Editable form after resume generation (optional feature)

---

## 🗂️ Project Structure

```
.
├── main.py                # Streamlit frontend
├── agent.py               # AI logic to generate PDF bytes
├── connection.py          # MySQL read/write logic
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🛠️ Requirements

- Python 3.8+
- MySQL Server
- Python Libraries:
  - streamlit
  - mysql-connector-python
  - fpdf (or reportlab or similar for PDF generation)

Install dependencies:

```bash
pip install -r requirements.txt
```

Example requirements.txt:

```text
streamlit
mysql-connector-python
fpdf
```

---

## ⚙️ Database Setup

1. Log in to MySQL and run the following:

```sql
CREATE DATABASE resume_builder;

USE resume_builder;

CREATE TABLE resumes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    pdf LONGBLOB
);
```

2. Update connection.py with your credentials:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="resume_builder"
)
```

---

## 🧪 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-resume-builder.git
cd ai-resume-builder
```

2. Run the Streamlit app:

```bash
streamlit run main.py
```

---

## ✏️ Optional Manual Resume Editing

You can add functionality to allow users to edit the generated resume manually by displaying the text before finalizing the PDF or by integrating tools like:

- pdfplumber (to extract PDF text)
- fpdf/reportlab (to regenerate PDF after edits)

---

## 📌 Notes

- Ensure your MySQL service is running before starting the app
- The app uses session state to store generated PDFs for inline display

---

