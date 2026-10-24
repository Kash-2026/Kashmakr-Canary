"""Structural verification suite for the deliverable.

Generated because the bundle ships content deliverables (markdown/
html) rather than a Python package. Every declared deliverable is
checked for existence and non-empty content.
"""

import os

import pytest


DELIVERABLES = ['report.md', 'report.html', 'index.html', 'requirements.txt', 'README.md']


def test_report_md_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'report.md')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"report.md is empty"

def test_report_html_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'report.html')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"report.html is empty"

def test_index_html_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"index.html is empty"

def test_requirements_txt_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"requirements.txt is empty"

def test_README_md_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'README.md')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"README.md is empty"

