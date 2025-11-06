# SmartTrendAI_Final

## Overview
AI-Powered Market Trend Analyzer (SmartTrendAI) compatible with Python 3.14.
Lightweight Streamlit web interface and console demo included.
This build avoids packages requiring compiled C extensions to ensure smooth installs on latest Python versions.

## Run locally (recommended)
1. Create and activate a virtual environment with Python 3.14:
   python -m venv venv
   Windows: venv\Scripts\activate
   macOS/Linux: source venv/bin/activate
2. Upgrade pip and install dependencies:
   pip install --upgrade pip setuptools wheel
   pip install -r requirements.txt
3. Download NLTK data (first run only):
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"
4. Run console demo:
   python src/main.py
5. Run the web app:
   streamlit run app.py

## Run on Google Colab
1. Upload project files to Colab or mount Google Drive.
2. Install requirements:
   !pip install --upgrade pip setuptools wheel
   !pip install -r requirements.txt
3. Download NLTK data in a cell:
   import nltk
   nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')
4. Run the demo (console):
   !python src/main.py
5. Running Streamlit in Colab is possible but requires extra setup (use ngrok or localtunnel).

## Files
- src/: python modules
- dataset/: sample dataset
- requirements.txt
- Project_Report.pdf : short project report
- README.md : this file