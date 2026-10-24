import json


class BusinessModelCanvas:
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
        for key in self.canvas:
            if key in venture_spec:
                self.canvas[key] = venture_spec[key]

    def check_completeness(self):
        return all(self.canvas[key] != "" for key in self.canvas)

    def compute_coherence_score(self):
        score = 0
        if (
            self.canvas["value_propositions"]
            and self.canvas["channels"]
            and self.canvas["revenue_streams"]
        ):
            score += 1
        return score

    def to_json(self):
        return json.dumps(self.canvas, indent=4)
