import re

GENDER_WORDS = [
    "male",
    "female",
    "mr",
    "mrs",
    "miss",
    "ms",
    "he",
    "she",
    "him",
    "her"
]

def anonymize_resume(text, entities):

    anonymous_text = text

    removed_items = []

    if entities["name"]:

        anonymous_text = anonymous_text.replace(
            entities["name"],
            "[NAME]"
        )

        removed_items.append("Candidate Name")

    for email in entities["emails"]:

        anonymous_text = anonymous_text.replace(
            email,
            "[EMAIL]"
        )

        removed_items.append("Email")

    for phone in entities["phones"]:

        anonymous_text = anonymous_text.replace(
            phone,
            "[PHONE]"
        )

        removed_items.append("Phone")

    for location in entities["locations"]:

        anonymous_text = anonymous_text.replace(
            location,
            "[LOCATION]"
        )

        removed_items.append("Location")

    words = anonymous_text.split()

    cleaned_words = []

    for word in words:

        if word.lower() not in GENDER_WORDS:
            cleaned_words.append(word)

    anonymous_text = " ".join(cleaned_words)

    fairness_score = 100 - len(set(removed_items))*5

    return anonymous_text, removed_items, fairness_score