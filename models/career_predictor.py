import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/career_dataset.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["skills"])

def predict_career(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = similarity.argmax()
    return df.iloc[index]["career"]