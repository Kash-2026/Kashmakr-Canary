"""Structural verification suite for the deliverable.

Generated because the bundle ships content deliverables (markdown/
html) rather than a Python package. Every declared deliverable is
checked for existence and non-empty content.
"""

import os

import pytest


DELIVERABLES = ['reel_script_product_launch.md', 'reel_script_behind_the_scenes.md', 'reel_script_customer_testimonial.md', 'index.html', 'requirements.txt', 'README.md']


def test_reel_script_product_launch_md_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'reel_script_product_launch.md')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"reel_script_product_launch.md is empty"

def test_reel_script_behind_the_scenes_md_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'reel_script_behind_the_scenes.md')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"reel_script_behind_the_scenes.md is empty"

def test_reel_script_customer_testimonial_md_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'reel_script_customer_testimonial.md')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"reel_script_customer_testimonial.md is empty"

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

