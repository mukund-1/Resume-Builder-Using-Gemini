import streamlit as st
import base64
from agent import resume_agent  # This should return PDF bytes
from connection import save_resume_to_mysql, get_resume_from_mysql  # DB functions

st.title("🧠 AI Resume Assistant")

# Sidebar or top menu for selection
option = st.radio("Choose an option", ["Build Resume", "Retrieve Resume"])

# --- Build Resume Section ---
if option == "Build Resume":
    st.subheader("📝 Build Your Resume")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    summary = st.text_area("Professional Summary")
    skills = st.text_input("Skills (comma-separated)")
    education = st.text_area("Education (e.g., Degree, University, Dates)")
    experience = st.text_area("Experience (e.g., Job Title, Company, Dates, Achievements)")

    if st.button("Generate Resume"):
        user_data = {
            "name": name,
            "email": email,
            "summary": summary,
            "skills": [s.strip() for s in skills.split(",") if s.strip()],
            "education": education,
            "experience": experience
        }

        pdf_bytes = resume_agent(user_data)
        st.session_state['pdf_bytes'] = pdf_bytes  # Save to session state

        # Save to DB
        save_resume_to_mysql(name, email, pdf_bytes)
        st.success("Resume saved to MySQL database successfully!")

    # Show PDF and download button if available
    if 'pdf_bytes' in st.session_state:
        pdf_bytes = st.session_state['pdf_bytes']

        # Display PDF
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

        # Download button
        st.download_button("Download Resume", data=pdf_bytes, file_name="resume.pdf", mime="application/pdf")

# --- Retrieve Resume Section ---
elif option == "Retrieve Resume":
    st.subheader("📂 Retrieve Your Resume")

    resume_id = st.number_input("Enter Resume ID", min_value=1, step=1)

    if st.button("Retrieve Resume"):
        pdf_data = get_resume_from_mysql(resume_id)  # returns tuple like (bytes,)
        if pdf_data:
            raw_pdf_bytes = pdf_data[0]

            # Display PDF
            base64_pdf = base64.b64encode(raw_pdf_bytes).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="500" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

            # Download button
            st.download_button("Download Resume", data=raw_pdf_bytes, file_name=f"resume_{resume_id}.pdf", mime="application/pdf")
        else:
            st.error("No resume found with that ID.")
