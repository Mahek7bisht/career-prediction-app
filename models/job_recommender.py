import pandas as pd
import os

# Correct path (safe handling)
file_path = os.path.join("data", "jobs_dataset.csv")

# Load dataset safely
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
else:
    print("ERROR: jobs_dataset.csv not found in data folder")
    df = pd.DataFrame(columns=["job_title", "skills", "link"])


def recommend_jobs(user_input):
    user_input = user_input.lower()
    matched_jobs = []

    for _, row in df.iterrows():
        job_skills = str(row["skills"]).lower()

        # Match any keyword
        if any(word in job_skills for word in user_input.split()):
            matched_jobs.append({
                "title": row["job_title"],
                "link": row["link"]
            })

    # If no match found → fallback (top 3 jobs)
    if not matched_jobs:
        for _, row in df.head(3).iterrows():
            matched_jobs.append({
                "title": row["job_title"],
                "link": row["link"]
            })

    return matched_jobs[:3]