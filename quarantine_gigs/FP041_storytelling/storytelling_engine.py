import random


class StorytellingEngine:
    def __init__(self):
        self.arcs = []

    def create_arc(self, topic):
        arc = {
            "topic": topic,
            "stakes": self.generate_stakes(),
            "beats": self.generate_beats(),
            "payoff": self.generate_payoff(),
            "retention_potential": self.calculate_retention_potential(),
        }
        self.arcs.append(arc)
        return arc

    def generate_stakes(self):
        stakes = [
            "The protagonist's life is at risk.",
            "The fate of the world hangs in the balance.",
            "The protagonist must overcome their past traumas.",
        ]
        return random.choice(stakes)

    def generate_beats(self):
        beats = [
            "The protagonist receives a mysterious letter.",
            "The protagonist embarks on a journey to a distant land.",
            "The protagonist faces a formidable enemy.",
        ]
        return random.choice(beats)

    def generate_payoff(self):
        payoff = [
            "The protagonist triumphs over adversity.",
            "The protagonist discovers a shocking truth.",
            "The protagonist finds love and acceptance.",
        ]
        return random.choice(payoff)

    def calculate_retention_potential(self):
        return random.uniform(0.5, 1.0)

    def rank_arcs(self):
        return sorted(self.arcs, key=lambda x: x["retention_potential"], reverse=True)
