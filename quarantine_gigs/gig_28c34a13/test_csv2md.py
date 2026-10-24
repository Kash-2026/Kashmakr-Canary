import pytest
from csv2md import convert_csv_to_markdown


def test_simple_conversion():
    csv_content = """header1,header2,header3
value1,value2,value3"""
    alignments = ["left", "center", "right"]
    max_width = 10
    expected = """|header1|header2|header3|
|--------|---------|----------|
|value1  | value2  |    value3|
"""
    assert convert_csv_to_markdown(csv_content, alignments, max_width) == expected


def test_wrapped_text():
    csv_content = """header
longvaluethatneedswrapping"""
    alignments = ["left"]
    max_width = 10
    expected = """|header|
|--------|
|longvalu|
|ethatnee|
|dswrappi|
|ng      |"""
    assert (
        convert_csv_to_markdown(csv_content, alignments, max_width)
        == expected
    )


def test_escaped_pipe():
    csv_content = """header
value|with|pipes"""
    alignments = ["left"]
    max_width = 10
    expected = """|header|
|--------|
|value\\|with\\|pipes|"""
    assert (
        convert_csv_to_markdown(csv_content, alignments, max_width)
        == expected
    )
