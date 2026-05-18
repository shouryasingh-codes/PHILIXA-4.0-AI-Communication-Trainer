from feature_extractor import extract_features
import pandas as pd
import joblib


# -------------------------
# LOAD MODEL
# -------------------------
model = joblib.load("philixa_model.pkl")
scaler = joblib.load("scaler.pkl")


# -------------------------
# FEEDBACK ENGINE
# -------------------------
def generate_feedback(features):

    strengths = []
    weaknesses = []

    # -------------------------
    # STRENGTHS
    # -------------------------
    if features["word_count"] >= 18:
        strengths.append(
            "Good detailed explanation."
        )

    if features["strong_verbs_count"] >= 1:
        strengths.append(
            "Good action-oriented wording."
        )

    if features["grammar_error_count"] == 0:
        strengths.append(
            "Grammar looks clean."
        )

    # -------------------------
    # WEAKNESSES
    # -------------------------
    if features["word_count"] < 18:
        weaknesses.append(
            "Explain your answer in more detail."
        )

    if features["avg_word_length"] < 4.5:
        weaknesses.append(
            "Use more descriptive vocabulary."
        )

    if features["strong_verbs_count"] == 0:
        weaknesses.append(
            "Use stronger action-oriented words."
        )

    grammar_errors = (
        features["grammar_error_count"]
    )

    if grammar_errors >= 2:
        weaknesses.append(
            "Your answer contains multiple grammar issues."
        )

    elif grammar_errors == 1:
        weaknesses.append(
            "Small grammar improvement possible."
        )

    return strengths, weaknesses


# -------------------------
# MAIN SCORER
# -------------------------
def score_answer(answer):

    # Extract features
    features = extract_features(answer)

    # Convert to dataframe
    user_input = pd.DataFrame([features])

    # Scale
    scaled_input = scaler.transform(
        user_input
    )

    # Prediction
    prediction = model.predict(
        scaled_input
    )

    probability = model.predict_proba(
        scaled_input
    )

    model_confidence = round(
        float(probability[0][1]),
        4
    )

    # Result
    if prediction[0] == 1:
        result = "Good Answer"

    else:
        result = "Needs Improvement"

    # Feedback
    strengths, weaknesses = (
        generate_feedback(features)
    )

    return {
        "result": result,

        "answer_quality_confidence":
            round(
                model_confidence * 100,
                2
            ),

        "strengths": strengths,

        "weaknesses": weaknesses
    }


# -------------------------
# TEST
# -------------------------
answer = input(
    "Enter your answer: "
)

result = score_answer(answer)

print("\nRESULT:")
print(result)