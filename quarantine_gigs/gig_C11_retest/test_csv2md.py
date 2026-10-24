import pytest
from csv2md import convert_csv_to_markdown


def test_simple_conversion():
    csv_content = """Name,Age,City
    John,30,New York
    Jane,25,Los Angeles"""
    expected_markdown = """|Name|Age|City|
    |-----------|-----|-----------------|
    |John|30|New York|
    |Jane|25|Los Angeles|"""
    assert convert_csv_to_markdown(csv_content) == expected_markdown


def test_quoted_fields():
    csv_content = (
        '"""Name","Age","City"\n"John","30","New York"\n"Jane","25","Los Angeles"'
    )
    expected_markdown = """|Name|Age|City|
    |-----------|-----|-----------------|
    |"John"|30|New York|
    |"Jane"|25|Los Angeles|"""
    assert convert_csv_to_markdown(csv_content) == expected_markdown


def test_escaped_pipes():
    csv_content = '"""Name","Age","City"\n"John","30","New York|USA"\n"Jane","25","Los Angeles|USA"'
    expected_markdown = """|Name|Age|City|
    |-----------|-----|-----------------|
    |"John"|30|New York\\|USA|
    |"Jane"|25|Los Angeles\\|USA|"""
    assert convert_csv_to_markdown(csv_content) == expected_markdown
