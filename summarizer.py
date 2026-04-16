import streamlit as st
import fitz
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Research AI", layout="centered")

st.title("📑 Instant Research Summarizer")
st.info(" Please just upload your PDF below and get the key findings for you.")

uploaded_file = st.file_uploader("Upload Research Paper", type="pdf")

if uploaded_file is not None:
    if not api_key:
        st.error("API Key missing! Make sure it's in the .env file.")
    else:
        # Step 1: Force Configuration
        genai.configure(api_key=api_key)
        
        # Step 2: Use the FULL model path (This fixes the 404 error)
        model = genai.GenerativeModel('gemini-2.5-flash')

        if st.button("Summarize Now"):
            with st.spinner("Analyzing the paper..."):
                try:
                    # PDF reading logic
                    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
                    text = "".join([page.get_text() for page in doc])

                    # Limiting text to avoid token overflow
                    prompt = f"Summarize this research paper for a professor. Give 1. Objective, 2. Method, 3. Key Results. Text: {text[:20000]}"
                    
                    # API Call
                    response = model.generate_content(prompt)
                    
                    st.subheader("📊 Summary Results")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"An error occurred: {e}")