import json


class AIService:
    def __init__(self, name, scope, price_floor, delivery_effort, margin):
        self.name = name
        self.scope = scope
        self.price_floor = price_floor
        self.delivery_effort = delivery_effort
        self.margin = margin

    def to_dict(self):
        return {
            "name": self.name,
            "scope": self.scope,
            "price_floor": self.price_floor,
            "delivery_effort": self.delivery_effort,
            "margin": self.margin,
        }


def package_service(name, scope, price_floor, delivery_effort, margin):
    service = AIService(name, scope, price_floor, delivery_effort, margin)
    return service.to_dict()


def save_service_to_manifest(service, filename="manifest.json"):
    with open(filename, "w") as f:
        json.dump(service, f, indent=4)
