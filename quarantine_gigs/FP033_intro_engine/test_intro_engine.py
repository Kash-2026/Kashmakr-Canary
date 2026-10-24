import pytest
from intro_engine import (
    generate_introduction,
    score_clarity,
    score_promise,
    evaluate_introduction,
)


def test_generate_introduction():
    intro = generate_introduction("climate change", "anecdote")
    assert "Once upon a time" in intro
    assert "Here's your thesis on climate change." in intro


def test_score_clarity():
    intro = "This is a test introduction for climate change."
    score = score_clarity(intro)
    assert score == 1


def test_score_promise():
    intro_with_thesis = "Here's your thesis on climate change."
    intro_without_thesis = "This is a test introduction for climate change."
    assert score_promise(intro_with_thesis) == 10
    assert score_promise(intro_without_thesis) == 1


def test_evaluate_introduction():
    intro = generate_introduction("climate change", "anecdote")
    evaluation = evaluate_introduction(intro)
    assert evaluation["clarity"] >= 1
    assert evaluation["promise"] == 10
