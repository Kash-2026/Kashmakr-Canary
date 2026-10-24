# gig_engine.py
from dataclasses import dataclass
from typing import List, Set
from datetime import datetime

@dataclass
class Gig:
    id: int
    title: str
    budget: float
    deadline: str
    skills: Set[str]

STANDARD_SKILLS = {
    "python",
    "data science",
    "machine learning",
    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "sql",
    "nosql",
}

def jaccard_similarity(skill_set: Set[str], standard_skills: Set[str]) -> float:
    if not skill_set or not standard_skills:
        return 0.0
    intersection = len(skill_set.intersection(standard_skills))
    union = len(skill_set.union(standard_skills))
    return intersection / union if union != 0 else 0.0

def estimate_budget(gig: Gig, complexity_tier: str) -> float:
    if not isinstance(gig, Gig) or not isinstance(complexity_tier, str):
        return 0.0
    complexity_factors = {"low": 0.8, "medium": 1.0, "high": 1.2}
    return gig.budget * complexity_factors.get(complexity_tier, 1.0)

def is_timeline_feasible(gig: Gig, milestones: List[str]) -> bool:
    if not milestones:
        return False
    return any("deliverable" in str(milestone).lower() for milestone in milestones)
