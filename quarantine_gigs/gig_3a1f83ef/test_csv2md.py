import pytest
from csv2md import csv2md


def test_simple_conversion():
    expected = """\
|header1|header2|
|-------|-------|
|value1 |value2 |
"""
    assert csv2md("sample.csv", alignment="l") == expected


def test_alignment():
    expected = """\
|header1|header2|
|-------|------:|
|value1 | value2|
"""
    assert csv2md("sample.csv", alignment="lr") == expected


def test_max_width():
    expected = """\
|header1|header2|
|-------|-------|
|value1 |this is a very long value that should be wrapped at 10 characters per line|
"""
    assert csv2md("sample.csv", alignment="l", max_width=10) == expected
