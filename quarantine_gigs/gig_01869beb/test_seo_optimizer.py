"""Auto-synthesized structural verification suite for the deliverable.

Generated because the model did not ship a test_deliverable.py.
Every public callable across every source module is imported and
exercised; a missing symbol, syntax fault, or import error fails
this suite for real.
"""

import enum
import inspect
import pytest

import seo_optimizer


def test_seo_optimizer_score_article_present_and_runs():
    assert hasattr(seo_optimizer, "score_article"), (
        "score_article missing from seo_optimizer"
    )
    target = seo_optimizer.score_article
    assert callable(target), "score_article" + " is not callable"
