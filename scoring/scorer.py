from feature_extractor import extract_features
import pandas as pd
import joblib
from xgboost import XGBClassifier



# STEP 1 — Load all saved model files


qt        = joblib.load("quantile_transformer.pkl")
scaler    = joblib.load("scaler.pkl")
lr_model  = joblib.load("philixa_lr_model.pkl")
le        = joblib.load("label_encoder.pkl")

xgb_model = XGBClassifier(verbosity=0)
xgb_model.load_model("philixa_xgb_model.json")


# STEP 2 — Feedback Engine


def generate_feedback(features, label):

    strengths  = []
    weaknesses = []

    # Did they explain WHY or HOW?
    if features["explanation_score"] >= 0.5:
        strengths.append("Clear explanation with cause / action / result.")
    else:
        weaknesses.append("Explain more — use words like 'because', 'so', 'the reason was'.")

    # Was the answer long enough?
    if features["word_count"] >= 25:
        strengths.append("Good answer length — enough detail.")
    elif features["word_count"] < 15:
        weaknesses.append("Too short — aim for at least 20-30 words.")

    # Did they use filler words?
    if features["filler_ratio"] == 0.0:
        strengths.append("No filler words — sounds confident.")
    elif features["filler_ratio"] > 0.1:
        weaknesses.append("Too many fillers (um, basically, kind of) — remove them.")

    # Was the language vague?
    if features["vague_language_score"] == 0.0:
        strengths.append("Language is specific and clear.")
    elif features["vague_language_score"] > 0.05:
        weaknesses.append("Too vague — avoid 'maybe', 'I think', 'something'.")

    # Did they use technical words?
    if features["technical_keyword_score"] >= 0.05:
        strengths.append("Good technical vocabulary.")
    else:
        weaknesses.append("Use more technical terms related to the problem.")

    # Grammar check
    errors = features["grammar_error_count"]
    if errors == 0:
        strengths.append("Grammar is clean.")
    elif errors >= 3:
        weaknesses.append(f"{errors} grammar issues found — review your sentences.")
    else:
        weaknesses.append(f"{errors} minor grammar issue — small fix needed.")

    # One-line tip based on final label
    tips = {
        "Strong"   : "✅ Strong — clear, specific, well-structured.",
        "Moderate" : "🟡 Decent — add more structure and specific details.",
        "Weak"     : "🔴 Weak — too vague or short. Use: situation → action → result.",
        "Off-topic": "⛔ Off-topic — answer didn't match the question. Try again.",
    }

    return strengths, weaknesses, tips.get(label, "")



# STEP 3 — Main Scorer


def score_answer(answer):

    # Turn the answer text into 6 numbers
    features   = extract_features(answer)
    user_input = pd.DataFrame([features])

    # QuantileTransform — same scale for all features
    qt_order = list(qt.feature_names_in_)
    user_qt  = pd.DataFrame(
        qt.transform(user_input[qt_order]),
        columns=qt_order
    )

    # StandardScale — normalize (needed for LR model)
    scaler_order = list(scaler.feature_names_in_)
    user_scaled  = scaler.transform(user_qt[scaler_order])

    # XGBoost predicts the label (primary model)
    xgb_enc        = xgb_model.predict(user_qt[qt_order])
    xgb_label      = le.inverse_transform(xgb_enc)[0]
    xgb_confidence = round(float(max(xgb_model.predict_proba(user_qt[qt_order])[0])) * 100, 2)

    # Logistic Regression cross-checks (secondary model)
    lr_label      = lr_model.predict(user_scaled)[0]
    lr_confidence = round(float(max(lr_model.predict_proba(user_scaled)[0])) * 100, 2)

    # Do both models agree?
    models_agree = (xgb_label == lr_label)

    # Generate human-readable feedback
    strengths, weaknesses, tip = generate_feedback(features, xgb_label)

    return {
        "label"        : xgb_label,
        "confidence"   : xgb_confidence,
        "lr_label"     : lr_label,
        "lr_confidence": lr_confidence,
        "models_agree" : models_agree,
        "tip"          : tip,
        "strengths"    : strengths,
        "weaknesses"   : weaknesses,
        "features"     : features,
    }


# STEP 4 — Quick Test (run directly)


if __name__ == "__main__":

    answer = input("Enter your answer: ")
    result = score_answer(answer)

    print("\n" + "=" * 50)
    print(f"  LABEL       : {result['label']}")
    print(f"  CONFIDENCE  : {result['confidence']}%")
    print(f"  LR CHECK    : {result['lr_label']} ({result['lr_confidence']}%)")
    print(f"  BOTH AGREE  : {'✅ Yes' if result['models_agree'] else '⚠️ No'}")
    print("=" * 50)
    print(f"\n{result['tip']}")

    print("\n✅ STRENGTHS:")
    for s in result["strengths"]:
        print(f"   • {s}")

    print("\n⚠️  WEAKNESSES:")
    for w in result["weaknesses"]:
        print(f"   • {w}")

    print("\n📊 FEATURES EXTRACTED:")
    for k, v in result["features"].items():
        print(f"   {k:<30} {v}")