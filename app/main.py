# External libraries
import streamlit as st
from streamlit_chat import message
import time
from PyPDF2 import PdfReader

# Internal file imports
from extract import extract_text
from embeddings import create_embeddings
from store import store_embeddings
# from qa import search_qa
from chat import chat_with_pdf

# Start of streamlit application
st.title("PDF QA Bot using Langchain")

# Intitialization
st.header("File upload")
file = st.file_uploader("Choose a file (PDF)", type="pdf", help="file to be parsed")

if file is not None:
    # @st.cache_data
    data = extract_text(file)
    # st.text(data, help="Extracted text from uploaded pdf")

    # Create, display, search and query the embeddings
    st.header("Create Embeddings")
    texts, embeddings, embeds_df = create_embeddings(
        data, st.secrets["OPENAI_API_KEY"]
    )
    st.text("Created successfully...")

    if store_embeddings(embeds_df):
        st.success("Data saved successfully...", icon="✅")
    else:
        st.error("Operation not successful. Please reach out to support...", icon="❌")

else:
    st.error("Upload the file to proceed further", icon="🚨")