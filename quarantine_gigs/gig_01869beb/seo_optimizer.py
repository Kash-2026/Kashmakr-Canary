import re
from collections import Counter
from typing import List, Tuple

def score_article(article: str, target_keyword: str, metadata_rules: dict) -> Tuple[int, List[str]]:
    """
    Scores an article based on SEO rules and returns prioritized edits.
    
    Parameters:
    - article: The article content as a string.
    - target_keyword: The target keyword to optimize for.
    - metadata_rules: A dictionary containing SEO rules.
    
    Returns:
    - score: An integer representing the SEO score.
    - edits: A list of prioritized edit suggestions.
    """
    score = 0
    edits = []

    # Rule 1: Keyword density
    article_lower = article.lower()
    keyword_density = article_lower.count(target_keyword.lower()) / len(article_lower.split())
    if keyword_density < metadata_rules.get('min_keyword_density', 0.01):
        score -= 10
        edits.append(f"Increase usage of '{target_keyword}' in the article.")

    # Rule 2: Title tag
    if not re.search(r"<title>.*{target_keyword}.*</title>", article, re.IGNORECASE):
        score -= 5
        edits.append(f"Include '{target_keyword}' in the title tag.")

    # Rule 3: Meta description
    if not re.search(r"<meta.*description.*{target_keyword}.*>", article, re.IGNORECASE):
        score -= 5
        edits.append(f"Include '{target_keyword}' in the meta description.")

    # Rule 4: Header tags
    header_tags = re.findall(r"<h[1-6]>.*</h[1-6]>", article, re.IGNORECASE)
    header_keyword_count = sum(target_keyword.lower() in tag.lower() for tag in header_tags)
    if header_keyword_count == 0:
        score -= 5
        edits.append(f"Include '{target_keyword}' in at least one header tag.")

    # Rule 5: Alt text for images
    alt_texts = re.findall(r'<img.*alt="([^"]+)".*>', article, re.IGNORECASE)
    alt_keyword_count = sum(target_keyword.lower() in text.lower() for text in alt_texts)
    if alt_keyword_count == 0:
        score -= 5
        edits.append(f"Include '{target_keyword}' in the alt text of at least one image.")

    return score, edits
