import streamlit as st
import pdfplumber
import pandas as pd
import io
import json
from openai import OpenAI
import os
from dotenv import load_dotenv
from AI_functions import extract_text_from_pdf, generate_sections, generate_roles, generate_one_pager

# --------------------
# Streamlit UI
# --------------------
st.title("📄 CV One Pager Generator")

uploaded_pdf = st.file_uploader("Upload a CV in PDF format", type=["pdf"])

if uploaded_pdf:
    with st.spinner("⏳ Generating one-pager summary..."):
        try:
            excel_data = generate_one_pager(uploaded_pdf)
            st.success("✅ Excel file generated successfully!")
            st.download_button(
                label="💾 Download Excel",
                data=excel_data,
                file_name="one_pager_summary.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        except Exception as e:
            st.error(f"❌ Error: {e}")
