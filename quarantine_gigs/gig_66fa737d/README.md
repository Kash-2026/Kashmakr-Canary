# Keyword Cluster Engine

## Overview
This engine clusters seed keywords by intent, assigns cluster labels, computes pairwise overlap, and emits an internal-link map with anchor suggestions.

## Usage
1. Cluster keywords and get cluster labels:
    ```python
    from keyword_cluster_engine import cluster_keywords
    keywords = ["buy shoes", "shoes for sale", "cheap shoes", "running shoes", "buy running shoes"]
    clusters, cluster_labels = cluster_keywords(keywords, n_clusters=2)
    ```
2. Compute pairwise overlap:
    ```python
    from keyword_cluster_engine import compute_overlap
    overlap = compute_overlap(keywords, clusters)
    ```
3. Generate internal-link map:
    ```python
    from keyword_cluster_engine import generate_link_map
    link_map = generate_link_map(keywords, clusters, cluster_labels)
    ```

## Testing
Run tests using pytest: