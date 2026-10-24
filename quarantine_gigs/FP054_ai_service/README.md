# AI Service Engine

This Python module packages AI capabilities into productized services with defined scope, price floor, delivery effort, and margin.

## Usage

1. Import the module:
    ```python
    from ai_service_engine import package_service, save_service_to_manifest
    ```

2. Package a service:
    ```python
    service = package_service("Image Recognition", "Identify objects in images", 1000, 50, 0.2)
    ```

3. Save the service to a manifest file:
    ```python
    save_service_to_manifest(service)
    ```

## Installation

Ensure you have Python 3.12 installed. No additional dependencies are required.