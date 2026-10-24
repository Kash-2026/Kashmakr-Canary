"""Acceptance suite for this deliverable."""
from __future__ import annotations

import youtube_description_engine

def test_build_description_substantive():
    transcript = "Learn python programming today with this easy tutorial on coding"
    keywords = ["python", "tutorial"]
    links = ["https://example.com/course"]
    desc = youtube_description_engine.build_description(transcript, keywords, links)
    assert len(desc) > 0
    assert "https://example.com/course" in desc
    assert "python" in desc.lower()

def test_score_keyword_coverage():
    desc = "learn python coding tutorial"
    keywords = ["python", "tutorial", "guide"]
    score = youtube_description_engine.score_keyword_coverage(desc, keywords)
    assert 0.0 < score <= 1.0
    assert round(score, 2) == 0.67
