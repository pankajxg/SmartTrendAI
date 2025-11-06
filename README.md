# SmartTrendAI_Stable

## Overview
AI-Powered Market Trend Analyzer (SmartTrendAI) compatible with Python 3.14 and Streamlit Cloud.
Includes automatic NLTK downloads to avoid LookupError on fresh environments.

## Features
- Top keywords frequency
- Sentiment analysis (VADER)
- Simple trend/growth scoring by date ranges
- Streamlit web UI with selectable text column

## Run locally
1. Create and activate a Python 3.14 venv
2. pip install --upgrade pip setuptools wheel
3. pip install -r requirements.txt
4. Download NLTK data (first run only) - the app also downloads automatically
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('omw-1.4')"
5. Run app:
   streamlit run app.py

## Deploy to Streamlit Cloud
1. Push repository to GitHub
2. Create new app on share.streamlit.io selecting this repo and main file app.py
3. Deploy

## Notes
The app defaults to a CSV column named 'text'. If your CSV uses another column name, select it in the sidebar.