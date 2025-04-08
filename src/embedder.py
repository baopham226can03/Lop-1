from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize
import pandas as pd
from tqdm import tqdm
from config import EMBEDDING_MODEL_NAME

model = SentenceTransformer(EMBEDDING_MODEL_NAME)

def tokenize_text(text):
    return tokenize(text)

def embed_text(text):
    return model.encode(text)

def embed_dataframe(df):
    tqdm.pandas()
    df["Câu hỏi tokenized"] = df["Câu hỏi"].apply(tokenize_text)
    df["embedding"] = df["Câu hỏi tokenized"].progress_apply(embed_text)
    return df
