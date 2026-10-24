import pytest
import channel_growth_engine


def test_project_growth_with_default_values():
    upload_cadence = 5
    topic_mix = 0.7
    retention_rate = 0.9
    initial_subscribers = 1000
    months = 6

    expected_growth = [1000, 1450, 1900, 2350, 2800, 3250, 3700]

    result = channel_growth_engine.project_growth(
        upload_cadence, topic_mix, retention_rate, initial_subscribers, months
    )

    assert result == expected_growth, "Projected growth does not match expected values"


def test_project_growth_with_zero_uploads():
    upload_cadence = 0
    topic_mix = 0.7
    retention_rate = 0.9
    initial_subscribers = 1000
    months = 6

    expected_growth = [1000, 900, 810, 729, 656, 590, 531]

    result = channel_growth_engine.project_growth(
        upload_cadence, topic_mix, retention_rate, initial_subscribers, months
    )

    assert result == expected_growth, (
        "Projected growth with zero uploads does not match expected values"
    )


def test_milestone_checkpoints_with_default_values():
    subscribers = [1000, 1450, 1900, 2350, 2800, 3250, 3700]
    milestones = [1500, 2000, 2500, 3000, 3500]

    expected_checkpoints = {1500: 1, 2000: 2, 2500: 3, 3000: 4, 3500: 5}

    result = channel_growth_engine.milestone_checkpoints(subscribers, milestones)

    assert result == expected_checkpoints, (
        "Milestone checkpoints do not match expected values"
    )


def test_milestone_checkpoints_with_no_milestones_reached():
    subscribers = [1000, 1100, 1200, 1300, 1400, 1500, 1600]
    milestones = [2000, 2500, 3000]

    expected_checkpoints = {}

    result = channel_growth_engine.milestone_checkpoints(subscribers, milestones)

    assert result == expected_checkpoints, (
        "Milestone checkpoints should be empty when no milestones are reached"
    )


def test_milestone_checkpoints_with_all_milestones_reached_in_first_month():
    subscribers = [5000, 5500, 6000, 6500, 7000, 7500, 8000]
    milestones = [5000, 5100, 5200, 5300, 5400]

    expected_checkpoints = {5000: 0, 5100: 0, 5200: 0, 5300: 0, 5400: 0}

    result = channel_growth_engine.milestone_checkpoints(subscribers, milestones)

    assert result == expected_checkpoints, (
        "Milestone checkpoints do not match expected values when all milestones are reached in the first month"
    )
