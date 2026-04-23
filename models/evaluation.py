import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from models.career_predictor import predict_career

def evaluate_model():
    df = pd.read_csv("data/career_dataset.csv")

    y_true = []
    y_pred = []

    for _, row in df.iterrows():
        input_text = row["skills"]
        actual = row["career"]
        predicted = predict_career(input_text)

        y_true.append(actual)
        y_pred.append(predicted)

    acc = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred)

    return acc, cm, y_true, y_pred