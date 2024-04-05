from PyPDF2 import PdfReader
import streamlit as st

@st.cache_data()
def parse_text(_file):
    """
        file: the PDF file to extract
    """
    content = ""
    reader = PdfReader(_file)
    numPages = len(reader.pages)

    # Scrape text from multiple pages
    for i in range(numPages):
        page = reader.pages[i]
        text = page.extract_text()
        content += text

    return content