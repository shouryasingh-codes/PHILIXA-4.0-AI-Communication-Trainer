import pandas as pd
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')


# HELPERS


FILLER_WORDS = [
    "um", "uh", "like", "you know", "basically",
    "literally", "actually", "honestly", "i mean",
    "kind of", "sort of", "right", "okay", "so",
    "just", "very", "really", "thing", "stuff"
]

TECHNICAL_KEYWORDS = [
    # Deployment
    "deployment", "rollback", "staging", "production", "canary",
    "migration", "pipeline", "release",

    # Debugging
    "debugging", "regression", "duplicate", "failures", "root cause",
    "mobile", "payment",

    # API / Contract
    "api", "contract", "token", "auth", "billing", "errors",
    "refresh", "logs", "endpoint", "customers",

    # Observability
    "alerts", "alert", "retry", "queue", "webhook", "incident",
    "observability", "batch", "tenant",

    # Data Pipeline
    "dashboard", "warehouse", "analytics", "query", "freshness",
    "report", "data", "load", "permission", "model",

    # Architecture
    "architecture", "platform", "tradeoff", "real-time",

    # Blocker / Sprint
    "blocker", "sprint", "dependency", "approval", "checklist",
    "frontend", "design", "planning",

    # Production Incident
    "outage", "handoff", "cadence", "status", "certificate",
    "hypothesis", "support",

    # Security
    "security", "rbac", "admin", "volume", "unusual", "false",
    "project",
    "system",
    "ai",
    "ml",
    "machine learning",
    "deep learning",
    "model",
    "communication",
    "customer",
    "analysis",
    "data",
    "engineering",
    "problem",
    "solution",
    "technical",
    "automation",
    "classifier",
    "prediction",
    "training"
]

VAGUE_WORDS = [
    "thing", "stuff", "maybe", "probably", "somehow",
    "something", "someone", "somewhere", "whenever",
    "whatever", "however", "anyway", "basically",
    "kind of", "sort of", "i think", "i guess",
    "not sure", "might be", "could be", "seems like"
]

EXPLANATION_MARKERS = [
    "because", "so", "therefore", "since", "due to",
    "as a result", "this means", "which means",
    "the reason", "in order to", "that is why",
    "which caused", "this happened", "the issue was",
    "the problem was", "the fix was", "i found that",
    "i noticed that", "i checked", "i confirmed"
     "the issue",          # 291x
    "root cause",         # 250x
    "likely cause",       # 150x
    "current issue",      # 150x
    "logs showed",        # 121x
    "the reason",         # 90x
    "i checked",          # 49x
    "blocked by",         # 44x
    "i found",            # 35x
    "monitor showed",     # 16x
    "review showed",      # 10x
    "profiles showed",    # 8x
    "the problem",        # 9x
    "because",
    "therefore",
    "due to",
    "as a result",
    "that is why",
    "which caused",
    "failed because",
    "error was",
    "issue was",
]



# MAIN EXTRACTOR

def extract_features(answer):

    if pd.isna(answer) or answer.strip() == "":
        return {
            "explanation_score":      0.0,
            "word_count":             0,
            "filler_ratio":           0.0,
            "vague_language_score":   0.0,
            "technical_keyword_score": 0.0,
            "grammar_error_count":    0
        }

    text       = answer.lower()
    words      = text.split()
    word_count = len(words)

    #1. explanation_score
    # How well the answer explains cause/action/result
    # Counts explanation marker phrases present in answer
    explanation_hits = sum(
        1 for marker in EXPLANATION_MARKERS
        if marker in text
    )
    # Normalize: cap at 4 markers = score 1.0
    explanation_score = round(
        min(explanation_hits / 4.0, 1.0), 4
    )

    # ── 2. word_count ────────────────────────────────────────
    # Raw word count — longer structured answers score higher
    # (log-transformed later in scorer before model input)

    # ── 3. filler_ratio ─────────────────────────────────────
    # Ratio of filler words to total words
    filler_hits = sum(
        1 for word in words
        if word.strip('.,!?;:"\'-') in FILLER_WORDS
    )
    # Also check multi-word fillers
    for phrase in ["you know", "kind of", "sort of", "i mean", "i guess", "not sure", "could be", "might be", "seems like"]:
        if phrase in text:
            filler_hits += 1

    filler_ratio = round(
        filler_hits / word_count
        if word_count > 0 else 0.0, 4
    )

    # ── 4. vague_language_score ──────────────────────────────
    # How vague/uncertain the answer sounds
    vague_hits = sum(
        1 for phrase in VAGUE_WORDS
        if phrase in text
    )
    vague_language_score = round(
        min(vague_hits / word_count, 1.0)
        if word_count > 0 else 0.0, 4
    )

    # ── 5. technical_keyword_score ───────────────────────────
    # Ratio of technical terms used
    tech_hits = sum(
        1 for word in words
        if word.strip('.,!?;:"\'-') in TECHNICAL_KEYWORDS
    )
    technical_keyword_score = round(
        min(tech_hits / word_count, 1.0)
        if word_count > 0 else 0.0, 4
    )

    # ── 6. grammar_error_count ───────────────────────────────
    matches            = tool.check(answer)
    grammar_error_count = len(matches)

    return {
        "explanation_score":        explanation_score,
        "word_count":               word_count,
        "filler_ratio":             filler_ratio,
        "vague_language_score":     vague_language_score,
        "technical_keyword_score":  technical_keyword_score,
        "grammar_error_count":      grammar_error_count
    }