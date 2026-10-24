import json
import networkx as nx


class AIWorkflowEngine:
    def __init__(self):
        self.workflow_graph = nx.DiGraph()

    def add_step(self, step_id, dependencies=None):
        if dependencies is None:
            dependencies = []
        self.workflow_graph.add_node(step_id)
        for dependency in dependencies:
            self.workflow_graph.add_edge(dependency, step_id)

    def validate_workflow(self):
        if not nx.is_directed_acyclic_graph(self.workflow_graph):
            raise ValueError("Workflow contains a cycle")
        return True

    def estimate_cost_and_latency(self):
        cost_and_latency = {}
        for node in self.workflow_graph.nodes:
            cost_and_latency[node] = {"cost": 1, "latency": 1}  # Placeholder values
        return cost_and_latency

    def generate_run_plan(self):
        run_plan = []
        for node in nx.topological_sort(self.workflow_graph):
            run_plan.append(node)
        return run_plan

    def to_manifest(self):
        manifest = {"steps": []}
        for step in self.workflow_graph.nodes:
            manifest["steps"].append(
                {
                    "id": step,
                    "dependencies": list(self.workflow_graph.predecessors(step)),
                }
            )
        return json.dumps(manifest, indent=4)
