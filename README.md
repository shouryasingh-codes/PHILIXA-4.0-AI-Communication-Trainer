# PHILIXA 4.0 — AI Communication Trainer

PHILIXA 4.0 is an AI-powered communication training system designed to help users improve interview and workplace communication skills.

The system evaluates a user's answer, analyzes communication quality, and provides feedback to help improve clarity, confidence, and overall answer quality.

This project is an upgraded version of PHILIXA 3.0, where the original ML-based communication scoring system has been reused and improved for a more interactive communication training experience.

---

## What PHILIXA 4.0 Does

- Evaluates user communication quality
- Uses Machine Learning to predict answer quality
- Detects strengths and weaknesses in responses
- Gives actionable feedback for improvement
- Simulates realistic communication evaluation

---

## How It Works

1. User enters an answer  
2. The system extracts communication-related features such as:
   - Word count
   - Sentence complexity
   - Strong action verbs
   - Grammar quality
   - Vocabulary patterns

3. A trained Machine Learning model evaluates answer quality

4. The system provides:
   - Communication result
   - Confidence score
   - Strengths
   - Weaknesses
   - Improvement feedback

---

## Tech Stack

- Python
- Scikit-learn
- Pandas
- Joblib
- LanguageTool
- Machine Learning (Logistic Regression)

---

## Project Structure

```text
PHILIXA_4/
│── app/
│── data/
│── memory/
│── prompts/
│── scoring/
│   ├── feature_extractor.py
│   ├── scorer.py
│   ├── philixa_model.pkl
│   └── scaler.pkl
│
│── simulation/
│── schemas.py
│── requirements.txt
│── README.md