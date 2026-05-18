import pandas as pd
import language_tool_python

tool = language_tool_python.LanguageTool('en-US')


# -------------------------
# HELPERS
# -------------------------
conjunctions = [
    'and', 'but', 'or', 'so',
    'because', 'though', 'while', 'when',
    'if', 'until', 'since', 'after',
    'before', 'which', 'that', 'who'
]

strong_verbs = [
    "started", "learned", "changed",
    "improved", "practiced", "worked",
    "realized", "stopped", "received",
    "invested", "failed", "recognized",
    "helped", "created", "developed",
    "used", "treated", "turned",
    "saved", "stayed", "expected",
    "reviewed", "noticed", "asked",
    "respected", "identified",
    "designed", "decided",
    "completed", "accepted",
    "volunteered", "pushed",
    "reduced", "discovered",
    "trusted", "focused",
    "prepared", "followed",
    "disagreed", "accelerated",
    "restructured", "shaped",
    "mattered", "dropped"
]

negations = [
    'no', 'not',
    'never', 'without'
]


# -------------------------
# REUSABLE FUNCTION
# -------------------------
def extract_features(answer):

    if pd.isna(answer):
        answer = ""

    # Word count
    words = answer.lower().split()
    word_count = len(words)

    # Avg word length
    total_length = 0

    for word in words:
        total_length += len(
            word.strip('.,!?;:"\'-')
        )

    avg_word_length = (
        total_length / word_count
        if word_count > 0 else 0
    )

    # Unique word ratio
    clean_words = []

    for word in words:
        clean_word = word.strip(
            '.,!?;:"\'-'
        )
        clean_words.append(clean_word)

    unique_words = set(clean_words)

    unique_word_ratio = (
        len(unique_words) / word_count
        if word_count > 0 else 0
    )

    # Sentence complexity
    sentence_complexity_score = 0

    for word in clean_words:
        if word in conjunctions:
            sentence_complexity_score += 1

    # Strong verbs count
    strong_verbs_count = 0

    for i in range(len(clean_words)):

        word = clean_words[i]

        if word in strong_verbs:

            prev1 = (
                clean_words[i - 1]
                if i >= 1 else ""
            )

            prev2 = (
                clean_words[i - 2]
                if i >= 2 else ""
            )

            if (
                prev1 not in negations
                and prev2 not in negations
            ):
                strong_verbs_count += 1

    # Grammar errors
    if answer.strip() == "":
        grammar_error_count = 0

    else:
        matches = tool.check(answer)
        grammar_error_count = len(matches)

    return {
        "word_count": word_count,
        "avg_word_length": round(
            avg_word_length, 6
        ),
        "unique_word_ratio":
            unique_word_ratio,
        "sentence_complexity_score":
            sentence_complexity_score,
        "strong_verbs_count":
            strong_verbs_count,
        "grammar_error_count":
            grammar_error_count
    }