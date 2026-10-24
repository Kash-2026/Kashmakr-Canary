import pytest
from keyword_cluster_engine import (
    cluster_keywords,
    compute_pairwise_similarity,
    compute_similarity,
    generate_internal_link_map,
    generate_anchor_text,
)


def test_cluster_keywords():
    keywords = ["buy shoes", "buy sneakers", "red shoes", "blue sneakers"]
    clusters = cluster_keywords(keywords, 0.5)
    assert len(clusters) == 2
    assert "buy shoes" in clusters
    assert "red shoes" in clusters["buy shoes"]


def test_compute_pairwise_similarity():
    keywords = ["buy shoes", "buy sneakers"]
    similarity_matrix = compute_pairwise_similarity(keywords)
    assert similarity_matrix["buy shoes"]["buy sneakers"] == 0.5


def test_compute_similarity():
    assert compute_similarity("buy shoes", "buy sneakers") == 0.5
    assert compute_similarity("red shoes", "blue sneakers") == 0.0


def test_generate_internal_link_map():
    clusters = {"buy shoes": ["buy shoes", "buy sneakers"]}
    link_map = generate_internal_link_map(clusters)
    assert link_map["buy shoes"]["buy sneakers"] == "Buy sneaker"


def test_generate_anchor_text():
    assert generate_anchor_text("buy shoes") == "Buy shoe"
    assert generate_anchor_text("red shoe") == "Red shoe"
