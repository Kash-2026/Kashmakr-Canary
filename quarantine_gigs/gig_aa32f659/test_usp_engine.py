import pytest
from usp_engine import (
    generate_usp,
    filter_duplicates,
    score_usp,
    generate_and_filter_usps,
)


def test_generate_usp():
    features = ["feature1", "feature2"]
    competitor_claims = ["claim1", "claim2"]
    usp_candidates = generate_usp(features, competitor_claims)
    assert len(usp_candidates) == 4
    assert "Our product feature1 unlike claim1." in usp_candidates
    assert "Our product feature2 unlike claim2." in usp_candidates


def test_filter_duplicates():
    usp_candidates = [
        "Our product feature1 unlike claim1.",
        "Our product feature1 unlike claim2.",
        "Our product feature2 unlike claim1.",
        "Our product feature2 unlike claim2.",
    ]
    filtered_usps = filter_duplicates(usp_candidates)
    assert len(filtered_usps) == 4
    assert "Our product feature1 unlike claim1." in filtered_usps
    assert "Our product feature2 unlike claim2." in filtered_usps


def test_score_usp():
    usp = "Our product feature1 unlike claim1."
    clarity_score, distinctiveness_score = score_usp(usp)
    assert isinstance(clarity_score, float)
    assert isinstance(distinctiveness_score, int)
    assert clarity_score > 0
    assert distinctiveness_score > 0


def test_generate_and_filter_usps():
    features = ["feature1", "feature2"]
    competitor_claims = ["claim1", "claim2"]
    scored_usps = generate_and_filter_usps(features, competitor_claims)
    assert len(scored_usps) == 4
    for usp, scores in scored_usps:
        assert isinstance(usp, str)
        assert isinstance(scores, tuple)
        assert len(scores) == 2
        assert isinstance(scores[0], float)
        assert isinstance(scores[1], int)
