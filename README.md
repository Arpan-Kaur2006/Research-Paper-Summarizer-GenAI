# 📑 Automated Research Paper Summarizer

A Python-based tool that uses **Generative AI (Google Gemini)** to extract and summarize key insights from academic research papers (PDFs).

🚀 **Features**
📄 Upload research papers in PDF format
⚡ Fast AI-powered summarization
🧠 Extracts:
Objective
Methodology
Key Results

🎯 **Clean and minimal Streamlit interface**
🔐 Secure API key handling using .env

🛠️ **Tech Stack**
Frontend/UI: Streamlit
Backend: Python
PDF Processing: PyMuPDF (fitz)
AI Model: Google Gemini API
Environment Management: python-dotenv
📂 Project Structure
├── app.py               # Main Streamlit application
├── .env                 # API key storage (not pushed to GitHub)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation

⚙️ **Installation & Setup**
1. Clone the repository
git clone https://github.com/your-username/research-summarizer.git
cd research-summarizer
2. Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install dependencies
pip install -r requirements.txt
4. Add your API key

Create a .env file in the root directory:

GEMINI_API_KEY=your_api_key_here
▶️ Run the App
streamlit run app.py

Then open the local URL shown in the terminal (usually http://localhost:8501).

🧪 **How It Works**
User uploads a PDF research paper
The app extracts text using PyMuPDF
Text is truncated to avoid token overflow
A structured prompt is sent to the Gemini model
The model returns a concise summary:
Objective
Method
Results

⚠️ **Limitations**
Only first ~20,000 characters of the PDF are processed
Performance depends on PDF text quality (scanned PDFs may fail)
Requires stable internet for API calls# 



