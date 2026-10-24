import pytest
import json
import giveaway_engine
import random


def test_create_giveaway_valid_input():
    engine = giveaway_engine.GiveawayEngine()
    giveaway = engine.create_giveaway(
        name="Test Giveaway",
        mechanics={"method": "random draw"},
        eligibility={"age": "18+"},
        budget=1000,
        fairness_score=85,
    )
    assert giveaway["name"] == "Test Giveaway"
    assert giveaway["mechanics"] == {"method": "random draw"}
    assert giveaway["eligibility"] == {"age": "18+"}
    assert giveaway["budget"] == 1000
    assert giveaway["fairness_score"] == 85


def test_create_giveaway_invalid_mechanics():
    engine = giveaway_engine.GiveawayEngine()
    with pytest.raises(
        ValueError, match="Mechanics and eligibility must be dictionaries."
    ):
        engine.create_giveaway(
            name="Invalid Giveaway",
            mechanics="not a dict",
            eligibility={"age": "18+"},
            budget=1000,
            fairness_score=85,
        )


def test_create_giveaway_invalid_eligibility():
    engine = giveaway_engine.GiveawayEngine()
    with pytest.raises(
        ValueError, match="Mechanics and eligibility must be dictionaries."
    ):
        engine.create_giveaway(
            name="Invalid Giveaway",
            mechanics={"method": "random draw"},
            eligibility="not a dict",
            budget=1000,
            fairness_score=85,
        )


def test_create_giveaway_invalid_budget():
    engine = giveaway_engine.GiveawayEngine()
    with pytest.raises(ValueError, match="Budget must be a non-negative number."):
        engine.create_giveaway(
            name="Invalid Giveaway",
            mechanics={"method": "random draw"},
            eligibility={"age": "18+"},
            budget=-100,
            fairness_score=85,
        )


def test_create_giveaway_invalid_fairness_score():
    engine = giveaway_engine.GiveawayEngine()
    with pytest.raises(ValueError, match="Fairness score must be between 0 and 100."):
        engine.create_giveaway(
            name="Invalid Giveaway",
            mechanics={"method": "random draw"},
            eligibility={"age": "18+"},
            budget=1000,
            fairness_score=105,
        )


def test_to_json():
    engine = giveaway_engine.GiveawayEngine()
    engine.create_giveaway(
        name="Test Giveaway 1",
        mechanics={"method": "random draw"},
        eligibility={"age": "18+"},
        budget=1000,
        fairness_score=85,
    )
    engine.create_giveaway(
        name="Test Giveaway 2",
        mechanics={"method": "lucky dip"},
        eligibility={"age": "21+"},
        budget=2000,
        fairness_score=90,
    )
    json_output = engine.to_json()
    expected_output = json.dumps(
        [
            {
                "name": "Test Giveaway 1",
                "mechanics": {"method": "random draw"},
                "eligibility": {"age": "18+"},
                "budget": 1000,
                "fairness_score": 85,
            },
            {
                "name": "Test Giveaway 2",
                "mechanics": {"method": "lucky dip"},
                "eligibility": {"age": "21+"},
                "budget": 2000,
                "fairness_score": 90,
            },
        ],
        indent=4,
    )
    assert json_output == expected_output
