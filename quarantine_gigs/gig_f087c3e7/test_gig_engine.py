from gig_engine import Gig, skill_matcher, budget_estimator, timeline_checker
import pytest


def test_skill_matcher():
    gig1 = Gig(
        id=1,
        title="Data Analysis",
        budget=1000,
        deadline="2023-12-31",
        skills=["Python", "SQL"],
    )
    gig2 = Gig(
        id=2,
        title="Web Development",
        budget=1500,
        deadline="2023-11-30",
        skills=["JavaScript", "HTML", "CSS"],
    )
    standard_skills = ["Python", "SQL", "JavaScript", "HTML", "CSS"]

    similarity1 = skill_matcher(gig1.skills, standard_skills)
    similarity2 = skill_matcher(gig2.skills, standard_skills)

    assert similarity1 == pytest.approx(0.4, abs=1e-6)
    assert similarity2 == pytest.approx(0.6, abs=1e-6)


def test_budget_estimator():
    gig1 = Gig(
        id=1,
        title="Data Analysis",
        budget=1000,
        deadline="2023-12-31",
        skills=["Python", "SQL"],
    )
    gig2 = Gig(
        id=2,
        title="Web Development",
        budget=1500,
        deadline="2023-11-30",
        skills=["JavaScript", "HTML"],
    )

    estimated_budget1 = budget_estimator(gig1)
    estimated_budget2 = budget_estimator(gig2)

    assert estimated_budget1 == 1200
    assert estimated_budget2 == 1800


def test_timeline_checker():
    gig1 = Gig(
        id=1,
        title="Data Analysis",
        budget=1000,
        deadline="2023-12-31",
        skills=["Python", "SQL"],
    )
    gig2 = Gig(
        id=2,
        title="Web Development",
        budget=1500,
        deadline="2023-11-30",
        skills=["JavaScript", "HTML"],
    )

    is_feasible1 = timeline_checker(gig1)
    is_feasible2 = timeline_checker(gig2)

    assert is_feasible1 is True
    assert is_feasible2 is False
