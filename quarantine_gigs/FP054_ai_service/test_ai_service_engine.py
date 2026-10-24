import pytest
from ai_service_engine import package_service, save_service_to_manifest
import os
import json


def test_package_service():
    service = package_service(
        "Image Recognition", "Identify objects in images", 1000, 50, 0.2
    )
    assert service["name"] == "Image Recognition"
    assert service["scope"] == "Identify objects in images"
    assert service["price_floor"] == 1000
    assert service["delivery_effort"] == 50
    assert service["margin"] == 0.2


def test_save_service_to_manifest():
    service = package_service(
        "Sentiment Analysis", "Analyze sentiment in text", 1500, 70, 0.25
    )
    save_service_to_manifest(service)

    with open("manifest.json", "r") as f:
        saved_service = json.load(f)

    assert saved_service["name"] == "Sentiment Analysis"
    assert saved_service["scope"] == "Analyze sentiment in text"
    assert saved_service["price_floor"] == 1500
    assert saved_service["delivery_effort"] == 70
    assert saved_service["margin"] == 0.25

    os.remove("manifest.json")
