from dataclasses import dataclass
from typing import List, Set, Dict, Any


@dataclass
class Gig:
    id: int
    title: str
    budget: float
    deadline: str
    skills: List[str]


STANDARD_SKILL_TAXONOMY: List[str] = [
    "python",
    "data analysis",
    "machine learning",
    "web development",
    "project management",
]
STANDARD_SKILLS: Set[str] = set(STANDARD_SKILL_TAXONOMY)


def jaccard_similarity(skill_set1: Any, skill_set2: Any) -> float:
    s1, s2 = set(skill_set1 or []), set(skill_set2 or [])
    return len(s1 & s2) / len(s1 | s2) if (s1 or s2) else 0.0


def skill_matcher(gig: Gig) -> float:
    return jaccard_similarity(gig.skills, STANDARD_SKILL_TAXONOMY)


COMPLEXITY_TIERS: Dict[str, float] = {"low": 1.0, "medium": 1.5, "high": 2.0}


def dynamic_budget_estimator(gig: Gig, complexity: str) -> float:
    return gig.budget * COMPLEXITY_TIERS.get(complexity, 1.0)


estimate_budget = dynamic_budget_estimator


def timeline_feasibility_checker(gig: Gig, milestones: Any) -> bool:
    if not milestones:
        return False
    if isinstance(milestones, dict):
        return True
    return any("deliverable" in str(m).lower() for m in milestones)


is_timeline_feasible = timeline_feasibility_checker
