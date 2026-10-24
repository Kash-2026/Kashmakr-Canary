import pytest
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial.distance import pdist, squareform
import keyword_cluster_engine


def test_cluster_keywords():
    keywords = ["apple pie", "banana bread", "cherry cake", "doughnut", "apple sauce"]
    clusters, cluster_labels = keyword_cluster_engine.cluster_keywords(
        keywords, n_clusters=2
    )
    assert len(clusters) == len(keywords)
    assert len(cluster_labels) == 2
    assert all(isinstance(label, str) for label in cluster_labels)


def test_compute_overlap():
    keywords = ["apple pie", "banana bread", "cherry cake", "doughnut", "apple sauce"]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(keywords)
    clusters = np.array([0, 1, 0, 1, 0])
    avg_overlap = keyword_cluster_engine.compute_overlap(tfidf_matrix, clusters)
    assert isinstance(avg_overlap, np.ndarray)
    assert len(avg_overlap) == 2


def test_generate_link_map():
    keywords = ["apple pie", "banana bread", "cherry cake", "doughnut", "apple sauce"]
    clusters = np.array([0, 1, 0, 1, 0])
    cluster_labels = ["fruity", "non-fruity"]
    link_map = keyword_cluster_engine.generate_link_map(
        keywords, clusters, cluster_labels
    )
    assert isinstance(link_map, dict)
    assert len(link_map) == 2
    assert all(isinstance(value, list) for value in link_map.values())
