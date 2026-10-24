import pytest
import storytelling_engine


def test_create_arc():
    engine = storytelling_engine.StorytellingEngine()
    arc = engine.create_arc("test topic")
    assert "topic" in arc
    assert "stakes" in arc
    assert "beats" in arc
    assert "payoff" in arc
    assert "retention_potential" in arc


def test_generate_stakes():
    engine = storytelling_engine.StorytellingEngine()
    stakes = engine.generate_stakes()
    assert stakes in [
        "The protagonist's life is at risk.",
        "The fate of the world hangs in the balance.",
        "The protagonist must overcome their past traumas.",
    ]


def test_generate_beats():
    engine = storytelling_engine.StorytellingEngine()
    beats = engine.generate_beats()
    assert beats in [
        "The protagonist receives a mysterious letter.",
        "The protagonist embarks on a journey to a distant land.",
        "The protagonist faces a formidable enemy.",
    ]


def test_generate_payoff():
    engine = storytelling_engine.StorytellingEngine()
    payoff = engine.generate_payoff()
    assert payoff in [
        "The protagonist triumphs over adversity.",
        "The protagonist discovers a shocking truth.",
        "The protagonist finds love and acceptance.",
    ]


def test_calculate_retention_potential():
    engine = storytelling_engine.StorytellingEngine()
    retention_potential = engine.calculate_retention_potential()
    assert 0.5 <= retention_potential <= 1.0


def test_rank_arcs():
    engine = storytelling_engine.StorytellingEngine()
    engine.create_arc("topic1")
    engine.create_arc("topic2")
    ranked_arcs = engine.rank_arcs()
    assert ranked_arcs == sorted(
        engine.arcs, key=lambda x: x["retention_potential"], reverse=True
    )
