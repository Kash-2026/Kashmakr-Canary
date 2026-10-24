# business_canvas_engine.py
class BusinessCanvasEngine:
    def __init__(self):
        self.canvas = {
            "customer_segments": "",
            "value_propositions": "",
            "channels": "",
            "customer_relationships": "",
            "revenue_streams": "",
            "key_resources": "",
            "key_activities": "",
            "key_partnerships": "",
            "cost_structure": "",
        }

    def fill_canvas(self, venture_spec):
        for block, content in venture_spec.items():
            if block in self.canvas:
                self.canvas[block] = content

    def is_complete(self):
        return all(self.canvas[block] for block in self.canvas)

    def compute_coherence_score(self):
        if not self.is_complete():
            return 0
        value_prop = self.canvas["value_propositions"]
        channels = self.canvas["channels"]
        revenue_streams = self.canvas["revenue_streams"]
        score = sum(1 for part in [value_prop, channels, revenue_streams] if part)
        return score / 3

# test_business_canvas_engine.py
import pytest
from business_canvas_engine import BusinessCanvasEngine

def test_fill_canvas():
    engine = BusinessCanvasEngine()
    venture_spec = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "Innovative gadgets",
        "channels": "Online store",
        "customer_relationships": "Loyalty program",
        "revenue_streams": "Direct sales",
        "key_resources": "R&D team",
        "key_activities": "Product development",
        "key_partnerships": "Suppliers",
        "cost_structure": "R&D costs",
    }
    engine.fill_canvas(venture_spec)
    for block, content in venture_spec.items():
        assert engine.canvas[block] == content, f"{block} was not filled correctly"

def test_is_complete():
    engine = BusinessCanvasEngine()
    venture_spec = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "Innovative gadgets",
        "channels": "Online store",
        "customer_relationships": "Loyalty program",
        "revenue_streams": "Direct sales",
        "key_resources": "R&D team",
        "key_activities": "Product development",
        "key_partnerships": "Suppliers",
        "cost_structure": "R&D costs",
    }
    engine.fill_canvas(venture_spec)
    assert engine.is_complete(), "Canvas is not complete after filling"

def test_compute_coherence_score():
    engine = BusinessCanvasEngine()
    venture_spec = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "Innovative gadgets",
        "channels": "Online store",
        "customer_relationships": "Loyalty program",
        "revenue_streams": "Direct sales",
        "key_resources": "R&D team",
        "key_activities": "Product development",
        "key_partnerships": "Suppliers",
        "cost_structure": "R&D costs",
    }
    engine.fill_canvas(venture_spec)
    score = engine.compute_coherence_score()
    assert score == 1.0, "Coherence score is incorrect"

    venture_spec_incomplete = {
        "customer_segments": "Tech enthusiasts",
        "value_propositions": "",
        "channels": "Online store",
        "customer_relationships": "Loyalty program",
        "revenue_streams": "Direct sales",
        "key_resources": "R&D team",
        "key_activities": "Product development",
        "key_partnerships": "Suppliers",
        "cost_structure": "R&D costs",
    }
    engine.fill_canvas(venture_spec_incomplete)
    score = engine.compute_coherence_score()
    assert score == 2 / 3, "Coherence score is incorrect for incomplete canvas"