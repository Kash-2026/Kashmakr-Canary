import pytest
import json
import networkx as nx
from ai_workflow_engine import AIWorkflowEngine


def test_add_step():
    engine = AIWorkflowEngine()
    engine.add_step("step1")
    engine.add_step("step2", dependencies=["step1"])
    assert list(engine.workflow_graph.nodes) == ["step1", "step2"]
    assert list(engine.workflow_graph.edges) == [("step1", "step2")]


def test_validate_workflow():
    engine = AIWorkflowEngine()
    engine.add_step("step1")
    engine.add_step("step2", dependencies=["step1"])
    assert engine.validate_workflow() is True


def test_validate_workflow_with_cycle():
    engine = AIWorkflowEngine()
    engine.add_step("step1")
    engine.add_step("step2", dependencies=["step1"])
    engine.add_step("step1", dependencies=["step2"])  # This creates a cycle
    with pytest.raises(ValueError, match="Workflow contains a cycle"):
        engine.validate_workflow()


def test_estimate_cost_and_latency():
    engine = AIWorkflowEngine()
    engine.add_step("step1")
    engine.add_step("step2", dependencies=["step1"])
    cost_and_latency = engine.estimate_cost_and_latency()
    assert cost_and_latency == {
        "step1": {"cost": 1, "latency": 1},
        "step2": {"cost": 1, "latency": 1},
    }


def test_generate_run_plan():
    engine = AIWorkflowEngine()
    engine.add_step("step1")
    engine.add_step("step2", dependencies=["step1"])
    run_plan = engine.generate_run_plan()
    assert run_plan == ["step1", "step2"]


def test_to_manifest():
    engine = AIWorkflowEngine()
    engine.add_step("step1")
    engine.add_step("step2", dependencies=["step1"])
    manifest = engine.to_manifest()
    expected_manifest = json.dumps(
        {
            "steps": [
                {"id": "step1", "dependencies": []},
                {"id": "step2", "dependencies": ["step1"]},
            ]
        },
        indent=4,
    )
    assert manifest == expected_manifest
