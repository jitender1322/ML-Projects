import requests


def analyze_grammar(text: str):

    url = "https://api.languagetool.org/v2/check"

    data = {
        "text": text,
        "language": "en-US"
    }

    response = requests.post(url, data=data)

    result = response.json()

    corrected_text = text

    grammar_feedback = []

    for match in result.get("matches", []):

        message = match.get("message")

        replacements = match.get("replacements")

        if replacements:

            correction = replacements[0]["value"]

            offset = match["offset"]
            length = match["length"]

            wrong_word = corrected_text[offset:offset+length]

            corrected_text = corrected_text.replace(
                wrong_word,
                correction,
                1
            )

            grammar_feedback.append({
                "wrong": wrong_word,
                "correct": correction,
                "message": message
            })

    fluency_score = max(1, 10 - len(grammar_feedback))

    return {
        "original_text": text,
        "corrected_text": corrected_text,
        "fluency_score": fluency_score,
        "grammar_feedback": grammar_feedback,
        "vocabulary_suggestions": [
            "Try using more advanced vocabulary."
        ]
    }