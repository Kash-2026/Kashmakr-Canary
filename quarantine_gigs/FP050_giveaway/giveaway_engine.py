import json


class GiveawayEngine:
    def __init__(self):
        self.specs = []

    def create_giveaway(self, name, mechanics, eligibility, budget, fairness_score):
        if not isinstance(mechanics, dict) or not isinstance(eligibility, dict):
            raise ValueError("Mechanics and eligibility must be dictionaries.")
        if not isinstance(budget, (int, float)) or budget < 0:
            raise ValueError("Budget must be a non-negative number.")
        if not isinstance(fairness_score, (int, float)) or not (
            0 <= fairness_score <= 100
        ):
            raise ValueError("Fairness score must be between 0 and 100.")

        giveaway = {
            "name": name,
            "mechanics": mechanics,
            "eligibility": eligibility,
            "budget": budget,
            "fairness_score": fairness_score,
        }
        self.specs.append(giveaway)
        return giveaway

    def to_json(self):
        return json.dumps(self.specs, indent=4)
