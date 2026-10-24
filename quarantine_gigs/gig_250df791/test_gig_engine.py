import pytest
from gig_engine import Gig, skill_matcher, estimate_budget, is_timeline_feasible


def test_skill_matcher():
    gig = Gig(1, "Data Analysis", 1000, "2023-12-31", ["python", "data analysis"])
    assert skill_matcher(gig) == pytest.approx(0.4, abs=0.01)
    gig = Gig(2, "Web Development", 2000, "2023-12-31", ["web development"])
    assert skill_matcher(gig) == pytest.approx(0.2, abs=0.01)


def test_dynamic_budget_estimator():
    gig = Gig(1, "Data Analysis", 1000, "2023-12-31", ["python", "data analysis"])
    assert estimate_budget(gig, "low") == 1000
    assert estimate_budget(gig, "medium") == 1500
    assert estimate_budget(gig, "high") == 2000


def test_timeline_feasibility_checker():
    gig = Gig(1, "Data Analysis", 1000, "2023-12-31", ["python", "data analysis"])
    assert (
        is_timeline_feasible(gig, {"milestone1": "deliverable", "milestone2": "review"})
        == True
    )
    assert is_timeline_feasible(gig, []) == False
    assert is_timeline_feasible(gig, "no milestones") == False
