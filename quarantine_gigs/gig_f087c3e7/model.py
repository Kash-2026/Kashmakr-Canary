"""
Freelance Gig Optimization Engine

This module provides a lightweight, deterministic implementation of the
core functionality required by the test suite:

* :class:`Gig` - a dataclass representing a freelance gig.
* :func:`skill_matcher` - computes Jaccard similarity between a gig's
  required skills and a standard skill taxonomy.
* :func:`budget_estimator` - estimates a dynamic budget based on the
  complexity tier of the gig.
* :func:`timeline_checker` - generates a simple milestone breakdown
  and verifies that the timeline is feasible.

The implementation is intentionally straightforward to keep the
behaviour predictable and fully deterministic, which is essential for
unit testing.
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Iterable, List, Sequence, Set

@dataclass(frozen=True)
class Gig:
    """
    Represents a freelance gig.

    Attributes
    ----------
    id : str
        Unique identifier for the gig.
    title : str
        Title or short description of the gig.
    budget : float
        The budget offered for the gig.
    deadline : datetime
        The due date for the gig.
    skills : Sequence[str]
        A list of skills required for the gig.
    """
    id: str
    title: str
    budget: float
    deadline: datetime
    skills: Sequence[str]

def skill_matcher(gig_skills: Iterable[str], taxonomy: Iterable[str]) -> float:
    """
    Compute the Jaccard similarity between the gig's skills and a
    standard skill taxonomy.

    Parameters
    ----------
    gig_skills : Iterable[str]
        Skills required by the gig.
    taxonomy : Iterable[str]
        Standard skill taxonomy.

    Returns
    -------
    float
        Jaccard similarity in the range [0.0, 1.0].
    """
    gig_set: Set[str] = set(map(str.lower, gig_skills))
    tax_set: Set[str] = set(map(str.lower, taxonomy))
    if not gig_set or not tax_set:
        return 0.0
    intersection = gig_set & tax_set
    union = gig_set | tax_set
    return len(intersection) / len(union)

def budget_estimator(gig: Gig) -> float:
    """
    Estimate a dynamic budget based on the gig's complexity tier.

    Complexity is determined by the number of distinct skills required.
    The estimator applies a tiered rate per skill:

    * 1-2 skills   : $50 per skill
    * 3-5 skills   : $70 per skill
    * 6+ skills    : $90 per skill

    The estimated budget is the product of the rate and the number of
    skills. The function returns the estimated budget rounded to two
    decimal places.

    Parameters
    ----------
    gig : Gig
        The gig for which to estimate the budget.

    Returns
    -------
    float
        Estimated budget in dollars.
    """
    skill_count = len(set(map(str.lower, gig.skills)))
    if skill_count <= 2:
        rate = 50.0
    elif skill_count <= 5:
        rate = 70.0
    else:
        rate = 90.0
    estimated = round(rate * skill_count, 2)
    return estimated

def timeline_checker(gig: Gig, milestones: int=3) -> List[datetime]:
    """
    Generate a milestone breakdown and verify that the timeline is feasible.

    The function creates ``milestones`` evenly spaced dates leading up to
    the gig's deadline. Each milestone must be at least one day apart.
    If the deadline is too close to the current date to accommodate the
    requested number of milestones, a :class:`ValueError` is raised.

    Parameters
    ----------
    gig : Gig
        The gig whose timeline is to be checked.
    milestones : int, optional
        Number of milestones to generate (default is 3).

    Returns
    -------
    List[datetime]
        A list of milestone dates in chronological order.

    Raises
    ------
    ValueError
        If the deadline is too soon to fit the requested milestones.
    """
    now = datetime.now()
    if gig.deadline <= now:
        raise ValueError('Deadline must be in the future.')
    total_days = (gig.deadline - now).days
    if total_days < milestones:
        raise ValueError(f'Deadline is too soon to fit {milestones} milestones.')
    interval = total_days // milestones
    milestone_dates: List[datetime] = []
    for i in range(1, milestones + 1):
        milestone = now + timedelta(days=i * interval)
        milestone_dates.append(milestone)
    if milestone_dates[-1] > gig.deadline:
        milestone_dates[-1] = gig.deadline
    return milestone_dates
__all__ = ['Gig', 'skill_matcher', 'budget_estimator', 'timeline_checker', 'Iterable', 'List', 'Sequence', 'Set', 'annotations', 'dataclass', 'datetime', 'timedelta']
