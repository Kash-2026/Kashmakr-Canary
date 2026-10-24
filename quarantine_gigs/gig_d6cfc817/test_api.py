"""
A minimal data aggregation module for the analytics dashboard.

This module provides a small set of functions that are used by the
JavaScript front‑end and are also imported by the test suite
(`test_deliverable.py`).  The functions operate on a simple JSON
structure that is expected to be present in the same directory as
this file.

The JSON data is assumed to be a list of objects with at least the
following keys:

* ``date``   - a string in ISO format (YYYY-MM-DD)
* ``category`` - a string identifying a category
* ``value``   - a numeric value

The functions below perform basic filtering and aggregation
operations that are sufficient for the unit tests and for
demonstration purposes.
"""
from __future__ import annotations
import json
import pathlib
from datetime import datetime
from typing import Any, Dict, Iterable, List, Tuple
__all__ = ['load_data', 'filter_by_date', 'aggregate_line', 'aggregate_bar', 'aggregate_donut', 'Any', 'Dict', 'Iterable', 'List', 'Tuple', 'annotations', 'datetime', 'json', 'pathlib']

def _data_path() -> pathlib.Path:
    """Return the absolute path to the bundled data.json file."""
    return pathlib.Path(__file__).with_name('data.json')

def load_data() -> List[Dict[str, Any]]:
    """
    Load the bundled JSON data.

    Returns
    -------
    list[dict]
        The parsed JSON data as a list of dictionaries.
    """
    path = _data_path()
    if not path.is_file():
        raise FileNotFoundError(f'Data file not found: {path}')
    with path.open('r', encoding='utf-8') as fp:
        return json.load(fp)

def filter_by_date(data: Iterable[Dict[str, Any]], start: str | datetime, end: str | datetime) -> List[Dict[str, Any]]:
    """
    Return a subset of *data* whose ``date`` field falls within the
    inclusive range defined by *start* and *end*.

    Parameters
    ----------
    data
        An iterable of dictionaries containing a ``date`` key.
    start, end
        Either ISO date strings or ``datetime`` objects.

    Returns
    -------
    list[dict]
        The filtered data.
    """
    if isinstance(start, str):
        start = datetime.fromisoformat(start)
    if isinstance(end, str):
        end = datetime.fromisoformat(end)
    result: List[Dict[str, Any]] = []
    for item in data:
        try:
            item_date = datetime.fromisoformat(item['date'])
        except (KeyError, ValueError):
            continue
        if start <= item_date <= end:
            result.append(item)
    return result

def aggregate_line(data: Iterable[Dict[str, Any]]) -> List[Tuple[str, float]]:
    """
    Aggregate data for a line chart.

    Returns a list of ``(date, total_value)`` tuples sorted by date.
    """
    totals: Dict[str, float] = {}
    for item in data:
        date = item.get('date')
        value = item.get('value', 0)
        if date is None:
            continue
        totals[date] = totals.get(date, 0) + float(value)
    return sorted([(date, totals[date]) for date in totals], key=lambda x: datetime.fromisoformat(x[0]))

def aggregate_bar(data: Iterable[Dict[str, Any]]) -> Dict[str, float]:
    """
    Aggregate data for a bar chart.

    Returns a mapping from category to the sum of values.
    """
    totals: Dict[str, float] = {}
    for item in data:
        category = item.get('category')
        value = item.get('value', 0)
        if category is None:
            continue
        totals[category] = totals.get(category, 0) + float(value)
    return totals

def aggregate_donut(data: Iterable[Dict[str, Any]]) -> Dict[str, float]:
    """
    Aggregate data for a donut chart.

    This is identical to ``aggregate_bar`` but kept separate for
    semantic clarity.
    """
    return aggregate_bar(data)
