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
    # Generate Excel only once
    if "excel_data" not in st.session_state:
        with st.spinner("⏳ Generating one-pager summary..."):
            try:
                excel_data = generate_one_pager(uploaded_pdf)
                st.session_state["excel_data"] = excel_data
                st.success("✅ Excel file generated successfully!")
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.stop()
    else:
        st.success("✅ Excel file already generated!")

    # 🟢 Download section (NO spinner)
    excel_data = st.session_state["excel_data"]
    download_clicked = st.download_button(
        label="💾 Download Excel",
        data=excel_data,
        file_name="one_pager_summary.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    if download_clicked:
        st.toast("🚀 Your download has started!")