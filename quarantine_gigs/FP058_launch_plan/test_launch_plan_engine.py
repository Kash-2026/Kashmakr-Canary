import pytest
from datetime import datetime, timedelta
import launch_plan_engine


def test_launch_plan_initialization():
    launch_plan = launch_plan_engine.create_launch_plan(
        "Product Launch",
        "2023-01-01",
        "2023-12-31",
        1000000,
        {"sales": 100000, "units_sold": 5000},
    )
    assert launch_plan.name == "Product Launch"
    assert launch_plan.start_date == datetime(2023, 1, 1)
    assert launch_plan.end_date == datetime(2023, 12, 31)
    assert launch_plan.budget == 1000000
    assert launch_plan.kpi_targets == {"sales": 100000, "units_sold": 5000}


def test_task_initialization():
    task = launch_plan_engine.Task("Marketing", "2023-01-01", "2023-03-31", 200000)
    assert task.name == "Marketing"
    assert task.start_date == datetime(2023, 1, 1)
    assert task.end_date == datetime(2023, 3, 31)
    assert task.budget == 200000


def test_add_task_to_launch_plan():
    launch_plan = launch_plan_engine.create_launch_plan(
        "Product Launch",
        "2023-01-01",
        "2023-12-31",
        1000000,
        {"sales": 100000, "units_sold": 5000},
    )
    task = launch_plan_engine.Task("Marketing", "2023-01-01", "2023-03-31", 200000)
    launch_plan.add_task(task)
    assert len(launch_plan.tasks) == 1
    assert launch_plan.tasks[0].name == "Marketing"


def test_validate_dependencies_valid():
    launch_plan = launch_plan_engine.create_launch_plan(
        "Product Launch",
        "2023-01-01",
        "2023-12-31",
        1000000,
        {"sales": 100000, "units_sold": 5000},
    )
    task1 = launch_plan_engine.Task("Marketing", "2023-01-01", "2023-03-31", 200000)
    task2 = launch_plan_engine.Task(
        "Sales", "2023-04-01", "2023-12-31", 500000, dependencies=["Marketing"]
    )
    launch_plan.add_task(task1)
    launch_plan.add_task(task2)
    launch_plan.validate_dependencies()


def test_validate_dependencies_invalid():
    launch_plan = launch_plan_engine.create_launch_plan(
        "Product Launch",
        "2023-01-01",
        "2023-12-31",
        1000000,
        {"sales": 100000, "units_sold": 5000},
    )
    task = launch_plan_engine.Task(
        "Sales", "2023-04-01", "2023-12-31", 500000, dependencies=["Marketing"]
    )
    launch_plan.add_task(task)
    with pytest.raises(
        ValueError, match="Task Sales has an invalid dependency: Marketing"
    ):
        launch_plan.validate_dependencies()


def test_launch_plan_to_json():
    launch_plan = launch_plan_engine.create_launch_plan(
        "Product Launch",
        "2023-01-01",
        "2023-12-31",
        1000000,
        {"sales": 100000, "units_sold": 5000},
    )
    json_str = launch_plan.to_json()
    assert (
        json_str
        == '{"name": "Product Launch", "start_date": "2023-01-01 00:00:00", "end_date": "2023-12-31 00:00:00", "budget": 1000000, "kpi_targets": {"sales": 100000, "units_sold": 5000}, "tasks": []}'
    )
