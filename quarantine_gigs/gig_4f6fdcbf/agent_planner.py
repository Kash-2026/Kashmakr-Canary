import json
from collections import deque, defaultdict
from typing import Dict, List, Any, Tuple


class Task:
    def __init__(self, name: str, dependencies: List[str] = None):
        self.name = name
        self.dependencies = dependencies if dependencies is not None else []
        self.state = "pending"

    def __repr__(self):
        return f"Task({self.name}, {self.dependencies}, {self.state})"


class AgentPlanner:
    def __init__(self):
        self.tasks = {}
        self.execution_order = []
        self.task_states = defaultdict(lambda: "pending")

    def add_task(self, name: str, dependencies: List[str] = None):
        if name in self.tasks:
            raise ValueError(f"Task {name} already exists")
        self.tasks[name] = Task(name, dependencies)

    def build_execution_order(self):
        in_degree = defaultdict(int)
        for task in self.tasks.values():
            for dependency in task.dependencies:
                in_degree[dependency] += 1

        queue = deque(
            [name for name, task in self.tasks.items() if in_degree[name] == 0]
        )
        self.execution_order = []

        while queue:
            current = queue.popleft()
            self.execution_order.append(current)
            for task_name, task in self.tasks.items():
                if current in task.dependencies:
                    in_degree[task_name] -= 1
                    if in_degree[task_name] == 0:
                        queue.append(task_name)

        if len(self.execution_order) != len(self.tasks):
            raise ValueError("Cycle detected in task dependencies")

    def execute_task(self, name: str):
        if self.task_states[name] != "pending":
            return False
        self.task_states[name] = "running"
        # Simulate task execution
        self.task_states[name] = "completed"
        return True

    def retry_failed_tasks(self):
        for name, state in self.task_states.items():
            if state == "failed":
                if self.execute_task(name):
                    self.task_states[name] = "completed"

    def get_task_state(self, name: str) -> str:
        return self.task_states[name]

    def to_json(self) -> str:
        return json.dumps(
            {
                "tasks": {name: task.__dict__ for name, task in self.tasks.items()},
                "execution_order": self.execution_order,
                "task_states": dict(self.task_states),
            }
        )

    @classmethod
    def from_json(cls, json_str: str) -> "AgentPlanner":
        data = json.loads(json_str)
        planner = cls()
        for name, task_data in data["tasks"].items():
            planner.add_task(name, task_data["dependencies"])
        planner.execution_order = data["execution_order"]
        planner.task_states = defaultdict(lambda: "pending", data["task_states"])
        return planner
