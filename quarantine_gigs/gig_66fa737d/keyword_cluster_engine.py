import numpy as np
from scipy.spatial.distance import pdist, squareform
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer

def cluster_keywords(keywords, n_clusters=5):
    """
    Cluster a list of seed keywords into `n_clusters` groups using TF‑IDF vectors
    and Agglomerative Clustering. Returns a tuple of:
    - `clusters`: array of cluster indices for each keyword
    - `cluster_labels`: a list of representative keywords for each cluster
    """
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(keywords)
    clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage="average")
    clusters = clustering.fit_predict(tfidf_matrix.toarray())
    cluster_labels = [
        keywords[np.where(clusters == i)[0][0]] for i in range(n_clusters)
    ]
    return clusters, cluster_labels

def compute_overlap(tfidf_matrix, clusters):
    """
    Compute the mean pairwise cosine overlap between keywords that belong to the
    same cluster. The function returns a NumPy array containing the single
    scalar mean overlap value so that callers can perform type checks against
    `np.ndarray` without changing the semantics of the calculation.
    """
    # Cosine distance matrix (1 - cosine similarity)
    overlap_matrix = squareform(pdist(tfidf_matrix.toarray(), metric="cosine"))
    np.fill_diagonal(overlap_matrix, 0)

    # Mask to keep only intra‑cluster distances
    mask = np.zeros_like(overlap_matrix, dtype=bool)
    for cluster in np.unique(clusters):
        indices = np.where(clusters == cluster)[0]
        mask[np.ix_(indices, indices)] = True

    # Compute the mean overlap PER CLUSTER (one value per cluster id),
    # so callers get an array whose length equals the number of clusters.
    per_cluster = []
    for cluster in np.unique(clusters):
        indices = np.where(clusters == cluster)[0]
        if len(indices) > 1:
            sub = overlap_matrix[np.ix_(indices, indices)]
            np.fill_diagonal(sub, 0)
            per_cluster.append(np.mean(sub))
        else:
            per_cluster.append(0.0)
    return np.array(per_cluster)

def generate_link_map(keywords, clusters, cluster_labels):
    """
    Build an internal link map where each cluster maps to a list of tuples
    containing the keyword and its cluster label. This map can be used to
    generate anchor suggestions for internal linking.
    """
    link_map = {}
    for i, cluster in enumerate(clusters):
        if cluster not in link_map:
            link_map[cluster] = []
        link_map[cluster].append((keywords[i], cluster_labels[cluster]))
    return link_map