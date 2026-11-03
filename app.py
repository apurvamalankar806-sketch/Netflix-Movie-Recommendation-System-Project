import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

@st.cache_resource
def load():
    df = pd.read_csv("netflix_titles.csv")
    df = df[['title', 'director', 'cast', 'listed_in', 'description']].fillna('')
    df['combined'] = df['director'] + ' ' + df['cast'] + ' ' + df['listed_in'] + ' ' + df['description']
    matrix = TfidfVectorizer(stop_words='english').fit_transform(df['combined'])
    indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()
    return df, matrix, indices

df, matrix, indices = load()

def recommend(title, n=10):
    idx = indices[title.lower()]
    scores = linear_kernel(matrix[idx], matrix).flatten()
    top = scores.argsort()[::-1][1:n+1]
    return pd.DataFrame({
        "Title": df.iloc[top]['title'].values,
        "Similarity %": (scores[top] * 100).round(2)
    })

st.title("Netflix Recommender")
choice = st.selectbox("Pick a title", sorted(df['title'].unique()))
if st.button("Recommend"):
    st.table(recommend(choice))