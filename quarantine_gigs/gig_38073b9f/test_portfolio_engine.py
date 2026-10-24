import pytest
from portfolio_engine import (
    calculate_skill_coverage,
    identify_skill_gaps,
    generate_portfolio_report,
)


def test_calculate_skill_coverage():
    projects = [
        {"skills": ["python", "data_analysis"]},
        {"skills": ["python", "machine_learning"]},
        {"skills": ["data_analysis", "machine_learning"]},
    ]
    result = calculate_skill_coverage(projects)
    assert result == {"python": 2, "data_analysis": 2, "machine_learning": 2}


def test_identify_skill_gaps():
    projects = [
        {"skills": ["python", "data_analysis"]},
        {"skills": ["machine_learning"]},
    ]
    required_skills = ["python", "data_analysis", "machine_learning", "statistics"]
    result = identify_skill_gaps(projects, required_skills)
    assert result == ["statistics"]


def test_generate_portfolio_report():
    projects = [
        {"skills": ["python", "data_analysis"]},
        {"skills": ["machine_learning"]},
    ]
    result = generate_portfolio_report(projects)
    assert result["total_projects"] == 2
    assert result["skill_coverage"] == {
        "python": 1,
        "data_analysis": 1,
        "machine_learning": 1,
    }
    assert result["skill_gaps"] == ["machine_learning"]
