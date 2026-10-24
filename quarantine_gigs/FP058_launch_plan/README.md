# Launch Plan Engine

## Overview
This engine allows you to create and manage product launch plans, including tasks, budget, KPI targets, and dependency validation.

## Usage
1. Create a launch plan:
    ```python
    plan = LaunchPlan("Product Launch", "2023-01-01", "2023-12-31", 1000000, {"sales": 100000, "users": 50000})
    ```
2. Add tasks to the plan:
    ```python
    task = Task("Marketing", "2023-02-01", "2023-03-31", 200000)
    plan.add_task(task)
    ```
3. Validate task dependencies:
    ```python
    plan.validate_dependencies()
    ```

## Testing
Run tests using pytest: