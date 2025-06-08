import re
import io
import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def markdown_to_html(text: str) -> str:
    # Convert **bold** markdown to <b>bold</b> html tags
    return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

def create_pdf_from_resume_text(resume_text: str) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                            rightMargin=40, leftMargin=40,
                            topMargin=60, bottomMargin=60)

    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    heading_style = ParagraphStyle(
        'Heading',
        parent=styles['Heading2'],
        spaceAfter=12,
        textColor=colors.darkblue,
    )

    flowables = []

    lines = resume_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Skip empty lines or lines with placeholders
        if not line or re.search(r"\[.*?\]", line):
            i += 1
            continue

        # Convert markdown bold to html tags
        html_line = markdown_to_html(line)

        # Heading lines surrounded by ** at start and end, e.g. **Summary**
        if line.startswith('**') and line.endswith('**'):
            heading_text = line.strip('* ')
            heading_text = markdown_to_html(heading_text)
            flowables.append(Paragraph(heading_text, heading_style))
            i += 1
            continue

        # Bullet points starting with - or *
        if line.startswith('- ') or line.startswith('* '):
            bullets = []
            while i < len(lines) and (lines[i].strip().startswith('- ') or lines[i].strip().startswith('* ')):
                bullet_text = lines[i].strip()[2:]
                bullet_text = markdown_to_html(bullet_text)
                bullets.append(ListItem(Paragraph(bullet_text, normal_style), bulletColor=colors.black))
                i += 1
            flowables.append(ListFlowable(bullets, bulletType='bullet', leftIndent=20))
            continue

        # Normal paragraph line
        flowables.append(Paragraph(html_line, normal_style))
        flowables.append(Spacer(1, 6))
        i += 1

    doc.build(flowables)
    buffer.seek(0)
    return buffer.getvalue()