from dataclasses import dataclass
from typing import List, Dict, Tuple
import datetime

@dataclass
class Gig:
    id: int
    title: str
    budget: float
    deadline: str
    skills: List[str]

STANDARD_SKILL_TAXONOMY = [
    "Python",
    "Data Analysis",
    "Machine Learning",
    "Web Development",
    "Cloud Computing",
]

def skill_matcher(gig_skills: List[str], standard_skills: List[str]) -> float:
    if not gig_skills or not standard_skills:
        return 0.0
    gig_skills_set = set(gig_skills)
    taxonomy_set = set(standard_skills)
    intersection = gig_skills_set.intersection(taxonomy_set)
    return len(intersection) / len(gig_skills_set.union(taxonomy_set)) if gig_skills_set.union(taxonomy_set) else 0.0

COMPLEXITY_TIERS = {"low": 1.0, "medium": 1.5, "high": 2.0}

def dynamic_budget_estimator(gig: Gig, complexity: str) -> float:
    if not isinstance(gig, Gig) or not isinstance(complexity, str):
        raise ValueError("Invalid input type")
    return gig.budget * COMPLEXITY_TIERS.get(complexity, 1.0)

def timeline_feasibility_checker(gig: Gig) -> Tuple[bool, Dict[str, str]]:
    """A gig is timeline-feasible when its deadline is at least 30 days after
    the project start (2023-12-01). Earlier deadlines are not feasible."""
    if not isinstance(gig, Gig):
        raise ValueError("Invalid input type")

    milestones = {
        "requirements_gathering": "2023-12-01",
        "design_phase": "2023-12-15",
        "development_phase": "2024-01-01",
        "testing_phase": "2024-01-15",
        "deployment": "2024-02-01",
    }

    gig_deadline = datetime.datetime.strptime(gig.deadline, "%Y-%m-%d")
    start = datetime.datetime.strptime(milestones["requirements_gathering"], "%Y-%m-%d")
    is_feasible = (gig_deadline - start).days >= 30
    return is_feasible, milestones


def budget_estimator(gig) -> float:
    """Estimate a gig's budget from its base budget and skill count.

    Each skill beyond the first adds 10% to the base budget, so a 1000-budget
    gig with 2 skills estimates to 1200.
    """
    skills = getattr(gig, "skills", []) or []
    multiplier = 1.0 + 0.1 * len(skills)
    return gig.budget * multiplier


def timeline_checker(gig) -> bool:
    """Return True when the gig's deadline is feasible for its budget."""
    feasible, _ = timeline_feasibility_checker(gig)
    return bool(feasible)
