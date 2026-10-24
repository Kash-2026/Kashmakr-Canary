import itertools
from typing import List, Dict, Tuple

def cluster_keywords(
    keywords: List[str], similarity_threshold: float
) -> Dict[str, List[str]]:
    """Greedy single-pass clustering.

    Each keyword joins the first existing cluster whose representative it is
    similar to (similarity >= threshold); otherwise it seeds a new cluster.
    Overlapping members are not merged across seeds, so the result has
    exactly one cluster per seed.
    """
    clusters: Dict[str, List[str]] = {}
    for keyword in keywords:
        placed = False
        for rep in list(clusters.keys()):
            if compute_similarity(keyword, rep) >= similarity_threshold:
                clusters[rep].append(keyword)
                placed = True
                break
        if not placed:
            clusters[keyword] = [keyword]
    return clusters


def compute_pairwise_similarity(keywords: List[str]) -> Dict[str, Dict[str, float]]:
    similarity_matrix = {}
    for keyword1, keyword2 in itertools.combinations(keywords, 2):
        similarity = compute_similarity(keyword1, keyword2)
        if keyword1 not in similarity_matrix:
            similarity_matrix[keyword1] = {}
        if keyword2 not in similarity_matrix:
            similarity_matrix[keyword2] = {}
        similarity_matrix[keyword1][keyword2] = similarity
        similarity_matrix[keyword2][keyword1] = similarity
    return similarity_matrix

def compute_similarity(keyword1: str, keyword2: str) -> float:
    if not keyword1 or not keyword2:
        return 0.0
    set1 = set(keyword1.lower().split())
    set2 = set(keyword2.lower().split())
    intersection = set1.intersection(set2)
    return len(intersection) / max(len(set1), len(set2))

def generate_internal_link_map(
    clusters: Dict[str, List[str]],
) -> Dict[str, Dict[str, str]]:
    link_map = {}
    for label, cluster in clusters.items():
        link_map[label] = {
            keyword: generate_anchor_text(keyword)
            for keyword in cluster
            if keyword!= label
        }
    return link_map

def _singularise(word: str) -> str:
    w = word.lower()
    return w[:-1] if w.endswith("s") and len(w) > 2 else w


def generate_anchor_text(keyword: str) -> str:
    words = keyword.split()
    if len(words) > 1:
        return words[0].capitalize() + " " + " ".join(_singularise(w) for w in words[1:])
    return _singularise(keyword).capitalize()