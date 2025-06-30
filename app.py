from flask import Flask, render_template, request
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load Q&A data from JSON
def load_knowledge_base(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

# Find best answer using cosine similarity
def get_best_answer(user_question, data):
    questions = [item["question"] for item in data]
    vectorizer = TfidfVectorizer().fit_transform(questions + [user_question])
    similarity = cosine_similarity(vectorizer[-1], vectorizer[:-1])
    best_idx = similarity.argmax()
    best_score = similarity[0][best_idx]

    if best_score < 0.2:
        return "Sorry, I couldn't find anything relevant."
    
    return data[best_idx]["answer"]

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        user_question = request.form["question"]
        data = load_knowledge_base("portfolio.json")  # <-- Ensure this file exists
        answer = get_best_answer(user_question, data)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
