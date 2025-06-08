import mysql.connector

def get_mysql_connection():
    return mysql.connector.connect(
        host="localhost",      # Change if your MySQL server is remote
        user="root",  # Your MySQL username
        password="5200",  # Your MySQL password
        database="resume_db"
    )

def save_resume_to_mysql(name, email, pdf_bytes):
    conn = get_mysql_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO resumes (name, email, pdf) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, email, pdf_bytes))
    conn.commit()
    cursor.close()
    conn.close()

def get_resume_from_mysql(resume_id):
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT pdf FROM resumes WHERE id = %s", (resume_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row  # (name, email, pdf_bytes) or None
