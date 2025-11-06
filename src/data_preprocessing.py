# src/data_preprocessing.py (No NLTK)
import re
import pandas as pd

# small built-in stopword list (you can expand)
STOP_WORDS = {
    'the','and','is','in','it','of','for','to','a','an','on','that','this','with','as','are','was','be','by','from'
}

def load_data(path):
    return pd.read_csv(path)

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def simple_tokenize(text):
    return re.findall(r"[a-zA-Z0-9']+", text)

def preprocess_dataframe(df, text_column='text'):
    df = df.copy()
    if text_column not in df.columns:
        df[text_column] = df.iloc[:, 0].astype(str)
    df['clean_text'] = df[text_column].fillna('').astype(str).apply(clean_text)
    df['tokens'] = df['clean_text'].apply(lambda t: [w for w in simple_tokenize(t) if w.lower() not in STOP_WORDS])
    df['processed'] = df['tokens'].apply(lambda tokens: ' '.join(tokens))
    return df
