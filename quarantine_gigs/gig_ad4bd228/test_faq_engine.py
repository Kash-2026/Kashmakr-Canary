import pytest
import faq_engine


def test_cluster_questions():
    notes = "What is the capital of France?\nWhat is the capital of Italy?\nWhat is the capital of Spain?\nWhat is the capital of France?"
    clusters = faq_engine.cluster_questions("Capitals", notes)
    assert len(clusters) == 3
    assert all(len(cluster) == 1 for cluster in clusters)


def test_extract_questions():
    notes = "What is the capital of France?\nThis is not a question.\nWhat is the capital of Italy?"
    questions = faq_engine.extract_questions(notes)
    assert questions == [
        "What is the capital of France?",
        "What is the capital of Italy?",
    ]


def test_deduplicate_questions():
    clusters = [
        ["What is the capital of France?"],
        ["What is the capital of France?", "What is the capital of Italy?"],
    ]
    deduplicated = faq_engine.deduplicate_questions(clusters)
    assert deduplicated == [
        ["What is the capital of France?"],
        ["What is the capital of France?", "What is the capital of Italy?"],
    ]


def test_answer_coverage_score():
    clusters = [["What is the capital of France?"], ["What is the capital of Italy?"]]
    answers = {
        "What is the capital of France?": "Paris",
        "What is the capital of Italy?": "Rome",
    }
    score = faq_engine.answer_coverage_score(clusters, answers)
    assert score == 1.0

    clusters = [["What is the capital of France?"], ["What is the capital of Italy?"]]
    answers = {"What is the capital of France?": "Paris"}
    score = faq_engine.answer_coverage_score(clusters, answers)
    assert score == 0.5
