import difflib

def cluster_questions(topic, notes):
    questions = extract_questions(notes)
    clusters = []
    for q in questions:
        best_match = None
        for cluster in clusters:
            similarity = difflib.SequenceMatcher(None, q, cluster[0]).ratio()
            if similarity > 0.7:
                best_match = cluster
                break
        if best_match:
            best_match.append(q)
        else:
            clusters.append([q])
    return clusters

def extract_questions(notes):
    if not notes:
        return []
    questions = [line for line in notes.split("\n") if line.strip().endswith("?")]
    return questions

def deduplicate_questions(clusters):
    deduplicated = []
    for cluster in clusters:
        unique_questions = list(set(cluster))
        deduplicated.append(unique_questions)
    return deduplicated

def answer_coverage_score(clusters, answers):
    score = 0
    total_questions = sum(len(cluster) for cluster in clusters)
    for cluster in clusters:
        for question in cluster:
            if question in answers:
                score += 1
    return score / total_questions if total_questions > 0 else 0