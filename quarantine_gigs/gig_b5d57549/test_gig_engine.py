import pytest
from gig_engine import Gig, jaccard_similarity, estimate_budget, is_timeline_feasible, STANDARD_SKILLS


def test_jaccard_similarity():
    skill_set = {"python", "data science"}
    assert jaccard_similarity(skill_set, STANDARD_SKILLS) == 2 / 10


def test_estimate_budget():
    gig = Gig(
        id=1,
        title="Data Analysis",
        budget=5000,
        deadline="2024-12-31",
        skills={"python", "data science"},
    )
    assert estimate_budget(gig, "low") == 4000
    assert estimate_budget(gig, "medium") == 5000
    assert estimate_budget(gig, "high") == 6000


def test_is_timeline_feasible():
    gig = Gig(
        id=1,
        title="Data Analysis",
        budget=5000,
        deadline="2024-12-31",
        skills={"python", "data science"},
    )
    milestones = ["Proposal", "Data Collection", "Analysis", "Report"]
    assert is_timeline_feasible(gig, milestones) == False
    milestones = [
        "Proposal",
        "Data Collection",
        "Analysis Deliverable",
        "Report Deliverable",
    ]
    assert is_timeline_feasible(gig, milestones) == True
