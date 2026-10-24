"""Structural verification suite for the deliverable.

Generated because the bundle ships content deliverables (markdown/
html) rather than a Python package. Every declared deliverable is
checked for existence and non-empty content.
"""

import os

import pytest


DELIVERABLES = ['README.md', 'requirements.txt', 'manifest.json', 'model.py', 'scraper.py', 'test_deliverable.py', 'contract.json']


def test_README_md_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'README.md')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"README.md is empty"

def test_requirements_txt_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"requirements.txt is empty"

def test_manifest_json_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'manifest.json')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"manifest.json is empty"

def test_model_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'model.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"model.py is empty"

def test_scraper_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'scraper.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"scraper.py is empty"

def test_test_deliverable_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_deliverable.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_deliverable.py is empty"

def test_contract_json_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'contract.json')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"contract.json is empty"

