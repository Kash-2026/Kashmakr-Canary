"""Structural verification suite for the deliverable.

Generated because the bundle ships content deliverables (markdown/
html) rather than a Python package. Every declared deliverable is
checked for existence and non-empty content.
"""

import os

import pytest


DELIVERABLES = ['test_scraper.py', 'package.json', 'models.py', 'README.md', 'test_email_builder.py', 'test_api.py', 'requirements.txt', 'test_dashboard.js', 'test_csv2md.py', 'manifest.json', 'jsdom_harness.cjs', 'test_invoice_pdf.py', 'model.py', 'app.js', 'data.json', 'index.html', 'test_deliverable.py', 'test_notes.py', 'test_bot.py', 'test_sheets_sync.py', 'contract.json']


def test_test_scraper_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_scraper.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_scraper.py is empty"

def test_package_json_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'package.json')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"package.json is empty"

def test_models_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'models.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"models.py is empty"

def test_README_md_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'README.md')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"README.md is empty"

def test_test_email_builder_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_email_builder.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_email_builder.py is empty"

def test_test_api_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_api.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_api.py is empty"

def test_requirements_txt_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"requirements.txt is empty"

def test_test_dashboard_js_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_dashboard.js')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_dashboard.js is empty"

def test_test_csv2md_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_csv2md.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_csv2md.py is empty"

def test_manifest_json_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'manifest.json')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"manifest.json is empty"

def test_jsdom_harness_cjs_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'jsdom_harness.cjs')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"jsdom_harness.cjs is empty"

def test_test_invoice_pdf_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_invoice_pdf.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_invoice_pdf.py is empty"

def test_model_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'model.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"model.py is empty"

def test_app_js_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'app.js')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"app.js is empty"

def test_data_json_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'data.json')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"data.json is empty"

def test_index_html_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'index.html')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"index.html is empty"

def test_test_deliverable_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_deliverable.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_deliverable.py is empty"

def test_test_notes_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_notes.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_notes.py is empty"

def test_test_bot_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_bot.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_bot.py is empty"

def test_test_sheets_sync_py_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'test_sheets_sync.py')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"test_sheets_sync.py is empty"

def test_contract_json_exists_and_nonempty():
    path = os.path.join(os.path.dirname(__file__), 'contract.json')
    assert os.path.isfile(path), f"{name} missing from bundle"
    assert os.path.getsize(path) > 0, f"contract.json is empty"

