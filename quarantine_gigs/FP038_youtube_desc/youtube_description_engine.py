import re

MAX_DESCRIPTION_LENGTH = 5000
MIN_KEYWORD_COVERAGE = 0.7
FRONT_LOAD_LENGTH = 100

def build_description(transcript, keywords, links):
    if not transcript or not keywords:
        raise ValueError("Transcript and keywords are required")

    keywords_set = set(keywords)
    words = transcript.split()
    description = []
    keyword_count = 0

    for word in words:
        if keyword_count / len(keywords_set) >= MIN_KEYWORD_COVERAGE:
            break
        if word.lower() in keywords_set:
            keyword_count += 1
        description.append(word)

        if len(" ".join(description)) > FRONT_LOAD_LENGTH:
            break

    front_loaded_description = " ".join(description[:FRONT_LOAD_LENGTH])
    remaining_description = " ".join(description[FRONT_LOAD_LENGTH:])
    description = front_loaded_description + " " + remaining_description
    description += " " + " ".join(links)

    if len(description) > MAX_DESCRIPTION_LENGTH:
        description = description[:MAX_DESCRIPTION_LENGTH]

    return description.strip()

def score_keyword_coverage(description, keywords):
    if not description or not keywords:
        return 0.0
    
    description_words = set(description.lower().split())
    keywords_set = set(keywords)
    common_words = description_words.intersection(keywords_set)
    return len(common_words) / len(keywords_set) if keywords_set else 1.0