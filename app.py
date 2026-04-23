from flask import Flask, render_template, request, jsonify
from models.career_predictor import predict_career
from models.job_recommender import recommend_jobs
from utils.preprocess import clean_text

from sklearn.metrics import confusion_matrix, accuracy_score
import pandas as pd

# ✅ CREATE APP FIRST
app = Flask(__name__)


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- CHAT ----------------
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    user_input = clean_text(user_input)

    career = predict_career(user_input)
    jobs = recommend_jobs(user_input)

    response = f"""
    <div class="career-box">🎯 {career}</div>
    <canvas id="skillChart" height="120"></canvas>
    """

    if jobs:
        for job in jobs:
            response += f"""
            <div class="job-card">
                <b>{job['title']}</b><br>
                <a href="{job['link']}" target="_blank">Apply Now</a>
            </div>
            """

    return jsonify({
        "reply": response,
        "labels": ["Python", "Data", "AI", "Design"],
        "values": [2, 3, 1, 0]
    })


# ---------------- METRICS ----------------
@app.route("/metrics", methods=["GET"])
def metrics():
    df = pd.read_csv("data/career_dataset.csv")

    y_true = []
    y_pred = []

    for _, row in df.iterrows():
        actual = row["career"]
        predicted = predict_career(row["skills"])

        y_true.append(actual)
        y_pred.append(predicted)

    acc = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred).tolist()

    return jsonify({
        "accuracy": round(acc, 2),
        "confusion_matrix": cm,
        "labels": list(set(y_true))
    })


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)