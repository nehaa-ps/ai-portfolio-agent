# 💼 Neha P S – AI Portfolio Assistant

An intelligent portfolio chatbot built with Flask that answers questions about my resume, skills, projects, and achievements using a local AI engine powered by cosine similarity and TF-IDF.

This is a professional and interactive way to showcase my profile.

---

## 🔍 Features

- 💬 Ask me questions like:
  - "What are your projects?"
  - "What internships have you completed?"
  - "What are your technical skills?"
  - "How can I contact you?"

- 🧠 Smart Q&A using TF-IDF + Cosine Similarity

- 🎨 Modern UI with:
  - Dark mode toggle 🌙
  - Animated avatar and layout
  - “👋 Know Me!” button with playful bio
  - Suggested question buttons
  - Typing indicator dots
  - Fully responsive design

---

## 🛠️ Tech Stack

| Layer       | Tools Used                              |
|-------------|------------------------------------------|
| Backend     | Python, Flask                            |
| NLP Engine  | scikit-learn (TF-IDF, Cosine Similarity) |
| Frontend    | HTML, CSS, JS                            |
| Knowledge   | `portfolio.json` (manual Q&A)            |

---

## 🗂️ Folder Structure

ai-portfolio-agent/
├── app.py
├── portfolio.json
├── requirements.txt
├── README.md
├── templates/
│ └── index.html
└── static/
├── style.css
└── avatar.png

yaml
Copy
Edit

---

## 🚀 Getting Started

1. **Clone the repository**:

```bash
git clone https://github.com/YOUR_USERNAME/neha-ai-portfolio.git
cd neha-ai-portfolio
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
python app.py
Open your browser and go to:
👉 http://localhost:5000

🧠 How It Works
The user submits a question

It is vectorized using TF-IDF along with the Q&A dataset

Cosine similarity identifies the closest matching question

The corresponding answer is returned instantly

📫 Contact Me
✉️ Email: nehaputhan@gmail.com

🔗 LinkedIn: linkedin.com/in/neha-p-s

🌟 Like This Project?
Star it ⭐, fork it 🍴, or use it as a template to build your own personal AI agent