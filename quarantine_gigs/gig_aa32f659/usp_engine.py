import re
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))


def generate_usp(features, competitor_claims):
    usp_candidates = []
    for feature in features:
        for claim in competitor_claims:
            usp = f"Our product {feature} unlike {claim}."
            usp_candidates.append(usp)
    return usp_candidates


def filter_duplicates(usp_candidates):
    filtered_usps = []
    token_counts = Counter()

    for usp in usp_candidates:
        tokens = word_tokenize(usp.lower())
        tokens = [
            token for token in tokens if token.isalnum() and token not in stop_words
        ]
        token_counts.update(tokens)

        if all(token_counts[token] == 1 for token in tokens):
            filtered_usps.append(usp)

    return filtered_usps


def score_usp(usp):
    words = usp.split()
    clarity_score = len(words) / (1 + sum(1 for word in words if word in stop_words))
    distinctiveness_score = sum(1 for word in words if word not in stop_words)
    return clarity_score, distinctiveness_score


def generate_and_filter_usps(features, competitor_claims):
    usp_candidates = generate_usp(features, competitor_claims)
    filtered_usps = filter_duplicates(usp_candidates)
    scored_usps = [(usp, score_usp(usp)) for usp in filtered_usps]
    return scored_usps
