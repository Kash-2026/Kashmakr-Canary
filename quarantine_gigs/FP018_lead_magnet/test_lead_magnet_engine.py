import pytest
from lead_magnet_engine import (
    generate_lead_magnet_concepts,
    get_format_delivery_choices,
    calculate_conversion_likelihood,
)


def test_generate_lead_magnet_concepts():
    concept = generate_lead_magnet_concepts(
        "small business owners", "cash flow management"
    )
    assert isinstance(concept, str)
    assert "small business owners" in concept
    assert "cash flow management" in concept


def test_get_format_delivery_choices():
    choice = get_format_delivery_choices()
    assert isinstance(choice, str)
    assert choice in [
        "PDF download",
        "Email series",
        "Webinar registration",
        "Video on-demand",
        "Interactive online tool",
    ]


def test_calculate_conversion_likelihood():
    score = calculate_conversion_likelihood("entrepreneurs", "marketing strategies")
    assert isinstance(score, float)
    assert 40 <= score <= 60
