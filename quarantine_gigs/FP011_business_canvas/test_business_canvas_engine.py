import json
import pytest
from business_canvas_engine import BusinessModelCanvas


def test_fill_canvas():
    venture_spec = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "Innovative solutions",
        "channels": "Online platforms",
        "customer_relationships": "Personal assistance",
        "revenue_streams": "Subscription model",
        "key_resources": "Intellectual property",
        "key_activities": "R&D",
        "key_partnerships": "Universities",
        "cost_structure": "High R&D costs",
    }
    canvas = BusinessModelCanvas()
    canvas.fill_canvas(venture_spec)
    for key in venture_spec:
        assert canvas.canvas[key] == venture_spec[key], f"{key} not filled correctly"


def test_check_completeness():
    venture_spec = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "Innovative solutions",
        "channels": "Online platforms",
        "customer_relationships": "Personal assistance",
        "revenue_streams": "Subscription model",
        "key_resources": "Intellectual property",
        "key_activities": "R&D",
        "key_partnerships": "Universities",
        "cost_structure": "High R&D costs",
    }
    canvas = BusinessModelCanvas()
    canvas.fill_canvas(venture_spec)
    assert canvas.check_completeness() == True, "Canvas should be complete"

    incomplete_venture_spec = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "Innovative solutions",
        "channels": "",
        "customer_relationships": "Personal assistance",
        "revenue_streams": "Subscription model",
        "key_resources": "Intellectual property",
        "key_activities": "R&D",
        "key_partnerships": "Universities",
        "cost_structure": "High R&D costs",
    }
    canvas.fill_canvas(incomplete_venture_spec)
    assert canvas.check_completeness() == False, "Canvas should not be complete"


def test_compute_coherence_score():
    venture_spec = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "Innovative solutions",
        "channels": "Online platforms",
        "customer_relationships": "Personal assistance",
        "revenue_streams": "Subscription model",
        "key_resources": "Intellectual property",
        "key_activities": "R&D",
        "key_partnerships": "Universities",
        "cost_structure": "High R&D costs",
    }
    canvas = BusinessModelCanvas()
    canvas.fill_canvas(venture_spec)
    assert canvas.compute_coherence_score() == 1, "Coherence score should be 1"

    incomplete_venture_spec = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "",
        "channels": "Online platforms",
        "customer_relationships": "Personal assistance",
        "revenue_streams": "Subscription model",
        "key_resources": "Intellectual property",
        "key_activities": "R&D",
        "key_partnerships": "Universities",
        "cost_structure": "High R&D costs",
    }
    canvas.fill_canvas(incomplete_venture_spec)
    assert canvas.compute_coherence_score() == 0, "Coherence score should be 0"


def test_to_json():
    venture_spec = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "Innovative solutions",
        "channels": "Online platforms",
        "customer_relationships": "Personal assistance",
        "revenue_streams": "Subscription model",
        "key_resources": "Intellectual property",
        "key_activities": "R&D",
        "key_partnerships": "Universities",
        "cost_structure": "High R&D costs",
    }
    canvas = BusinessModelCanvas()
    canvas.fill_canvas(venture_spec)
    json_output = canvas.to_json()
    expected_json = json.dumps(venture_spec, indent=4)
    assert json_output == expected_json, "JSON output does not match expected JSON"
