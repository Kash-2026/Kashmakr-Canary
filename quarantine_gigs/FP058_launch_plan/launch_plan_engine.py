import json
from datetime import datetime, timedelta


class LaunchPlan:
    def __init__(self, name, start_date, end_date, budget, kpi_targets):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.budget = budget
        self.kpi_targets = kpi_targets
        self.tasks = []

    def add_task(self, task):
        if not task:
            raise ValueError("Task cannot be empty")
        self.tasks.append(task)

    def validate_dependencies(self):
        for task in self.tasks:
            if task.dependencies:
                for dependency in task.dependencies:
                    if not any(t for t in self.tasks if t.name == dependency):
                        raise ValueError(
                            f"Task {task.name} has an invalid dependency: {dependency}"
                        )

    def to_json(self):
        return json.dumps(self.__dict__, default=str)


class Task:
    def __init__(self, name, start_date, end_date, budget, dependencies=None):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.budget = budget
        self.dependencies = dependencies if dependencies else []


def create_launch_plan(name, start_date, end_date, budget, kpi_targets):
    return LaunchPlan(name, start_date, end_date, budget, kpi_targets)
