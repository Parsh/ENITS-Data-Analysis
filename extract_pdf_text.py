#!/usr/bin/env python3
import pdfplumber
import os
import sys

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file using pdfplumber."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
            return text
    except Exception as e:
        return f"Error extracting text from {pdf_path}: {str(e)}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 extract_pdf_text.py <pdf_file>")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    if not os.path.exists(pdf_file):
        print(f"File {pdf_file} does not exist")
        sys.exit(1)
    
    text = extract_text_from_pdf(pdf_file)
    print(text)

if __name__ == "__main__":
    main()
