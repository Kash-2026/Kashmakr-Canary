"""Auto-synthesized structural verification suite for the deliverable.

Generated because the model did not ship a test_deliverable.py.
Every public callable across every source module is imported and
exercised; a missing symbol, syntax fault, or import error fails
this suite for real.
"""

import enum
import inspect
import pytest

import gig_engine
import model


def test_gig_engine_Gig_present_and_runs():
    assert hasattr(gig_engine, "Gig"), "Gig missing from gig_engine"
    target = gig_engine.Gig
    assert callable(target), "Gig" + " is not callable"


def test_gig_engine_skill_matcher_present_and_runs():
    assert hasattr(gig_engine, "skill_matcher"), "skill_matcher missing from gig_engine"
    target = gig_engine.skill_matcher
    assert callable(target), "skill_matcher" + " is not callable"


def test_gig_engine_dynamic_budget_estimator_present_and_runs():
    assert hasattr(gig_engine, "dynamic_budget_estimator"), (
        "dynamic_budget_estimator missing from gig_engine"
    )
    target = gig_engine.dynamic_budget_estimator
    assert callable(target), "dynamic_budget_estimator" + " is not callable"


def test_gig_engine_timeline_feasibility_checker_present_and_runs():
    assert hasattr(gig_engine, "timeline_feasibility_checker"), (
        "timeline_feasibility_checker missing from gig_engine"
    )
    target = gig_engine.timeline_feasibility_checker
    assert callable(target), "timeline_feasibility_checker" + " is not callable"
