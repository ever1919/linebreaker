import pdfplumber
import pandas as pd
from openai import OpenAI
import json
import os
import sys
from dotenv import load_dotenv
from AI_functions import extract_text_from_pdf, generate_sections, generate_roles, generate_one_pager


if len(sys.argv) < 2:
    print("Usage: python main.py <path_to_pdf>")
    sys.exit(1)
else:
    pdf_path = sys.argv[1]

if __name__ == "__main__":
    input_dir = "data/input"
    output_dir = "data/output"
    os.makedirs(output_dir, exist_ok=True)

for file_name in os.listdir(input_dir):
    if file_name.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name.replace(".pdf", "_one_pager.xlsx"))
        generate_one_pager(pdf_path, output_path)