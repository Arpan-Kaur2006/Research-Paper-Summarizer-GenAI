# 📑 Automated Research Paper Summarizer

A Python-based tool that uses **Generative AI (Google Gemini)** to extract and summarize key insights from academic research papers (PDFs).

## ✨ Features
- **PDF Text Extraction:** Uses `PyMuPDF` to parse high-density academic text.
- **AI-Powered Insights:** Connects to Gemini API to distill papers into:
  - Main Objective
  - Top 3 Key Findings
  - Methodology Used

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Add your Gemini API Key in `summarizer.py`.
4. Place your PDF as `paper.pdf` and run: `python3 summarizer.py`

## 🛠️ Tech Stack
- **Language:** Python
- **AI Model:** Google Gemini (1.5 Flash/Pro)
- **Library:** PyMuPDF (fitz)