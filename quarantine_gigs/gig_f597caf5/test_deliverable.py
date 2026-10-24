import pytest
from model import analyze_competitors


def test_analyze_competitors():
    competitors = [
        {
            "name": "Competitor A",
            "marketShare": "30%",
            "strengths": "Strong brand, High customer loyalty",
            "weaknesses": "High prices",
        },
        {
            "name": "Competitor B",
            "marketShare": "25%",
            "strengths": "Innovative products, Agile development",
            "weaknesses": "Limited market presence",
        },
        {
            "name": "Competitor C",
            "marketShare": "20%",
            "strengths": "Cost leadership, Efficient supply chain",
            "weaknesses": "Perceived lower quality",
        },
    ]

    result = analyze_competitors(competitors)

    assert len(result) == 3
    assert result[0]["market_share"] == 30
    assert result[1]["market_share"] == 25
    assert result[2]["market_share"] == 20
