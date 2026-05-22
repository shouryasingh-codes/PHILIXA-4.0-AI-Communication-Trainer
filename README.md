# PHILXA 4.0 - AI Communication Trainer

PHILXA 4.0 is an AI-powered communication training system designed to help users improve workplace communication skills.

The MVP focuses on one Corporate World room where a user enters a live office meeting, responds to workplace prompts, and receives scoring plus coaching feedback.

This project reuses the PHILXA scoring work and expands it into a more interactive communication-training experience.

## MVP Scope

The MVP is locked to:

- Room: Corporate World
- Scenario: team discussion / office meeting
- AI roles: Boss, Manager, and Colleague
- User role: team member
- Score areas: confidence, grammar, clarity, and structure

Day 1 planning docs:

- [MVP roadmap](docs/mvp_roadmap.md)
- [MVP scope](docs/mvp_scope.md)
- [User test flow](docs/user_test_flow.md)
- [Day 1 execution checklist](docs/day_01_execution.md)

## What PHILXA 4.0 Does

- Evaluates user communication quality
- Uses machine learning to predict answer quality
- Detects strengths and weaknesses in responses
- Gives actionable feedback for improvement
- Simulates realistic workplace communication evaluation

## How It Works

1. The room starts with a short AI-to-AI office conversation.
2. The user enters and responds as a team member.
3. The system stores conversation turns in a structured format.
4. The scoring layer extracts communication features such as:
   - word count
   - sentence complexity
   - strong action verbs
   - grammar quality
   - vocabulary patterns
5. The system evaluates the answer.
6. The user receives:
   - communication result
   - confidence score
   - strengths
   - weaknesses
   - improvement feedback

## Tech Stack

- Python
- Scikit-learn
- Pandas
- Joblib
- LanguageTool
- Streamlit or Gradio for the first UI

## Project Structure

```text
PHILXA_4/
  app/
  data/
  docs/
    day_01_execution.md
    mvp_roadmap.md
    mvp_scope.md
    user_test_flow.md
  memory/
  prompts/
  scoring/
    feature_extractor.py
    scorer.py
    philixa_model.pkl
    scaler.pkl
  simulation/
  schemas.py
  requirements.txt
  README.md
```

## Next Build Step

Start Day 2 by replacing the dictionary-only schemas in `schemas.py` with typed models for messages, sessions, roles, scores, and feedback.
