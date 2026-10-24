"""model.py

A minimal data model for the analytics dashboard.
The module provides utilities for loading JSON data, filtering by a date range,
and computing simple aggregates that can be used by the front‑end charts.
"""
from __future__ import annotations
import json
from datetime import datetime, date
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple
__all__ = ['load_data', 'filter_by_date', 'aggregate_line', 'aggregate_bar', 'aggregate_donut', 'Any', 'Dict', 'Iterable', 'List', 'Path', 'Tuple', 'annotations', 'date', 'datetime', 'json']

def _parse_date(value: str | datetime) -> datetime:
    """Parse a date string in ISO format or return a datetime instance."""
    if isinstance(value, datetime):
        return value
    try:
        return datetime.fromisoformat(value)
    except Exception as exc:
        raise ValueError(f'Invalid date format: {value}') from exc

def load_data(file_path: str | Path) -> List[Dict[str, Any]]:
    """
    Load JSON data from *file_path*.

    The JSON file is expected to contain an array of objects.  Each object
    must contain at least a ``date`` field (ISO 8601 string) and a numeric
    ``value`` field.  Additional fields are preserved.

    Parameters
    ----------
    file_path : str | Path
        Path to the JSON file.

    Returns
    -------
    List[Dict[str, Any]]
        The parsed data records with ``date`` converted to ``datetime`` and
        ``value`` converted to ``float``.
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f'Data file not found: {file_path}')
    with path.open('r', encoding='utf-8') as fh:
        data = json.load(fh)
    if not isinstance(data, list):
        raise ValueError('JSON root must be an array of records')
    parsed: List[Dict[str, Any]] = []
    for rec in data:
        if 'date' not in rec or 'value' not in rec:
            raise ValueError("Each record must contain 'date' and 'value' keys")
        parsed_rec: Dict[str, Any] = dict(rec)
        parsed_rec['date'] = _parse_date(rec['date'])
        try:
            parsed_rec['value'] = float(rec['value'])
        except Exception as exc:
            raise ValueError(f'Invalid numeric value: {rec['value']}') from exc
        parsed.append(parsed_rec)
    return parsed

def filter_by_date(data: Iterable[Dict[str, Any]], start: str | datetime, end: str | datetime) -> List[Dict[str, Any]]:
    """
    Return records whose ``date`` falls within the inclusive range [start, end].

    Parameters
    ----------
    data : Iterable[Dict[str, Any]]
        The dataset to filter.
    start : str | datetime
        Start of the date range (inclusive).
    end : str | datetime
        End of the date range (inclusive).

    Returns
    -------
    List[Dict[str, Any]]
        Filtered records.
    """
    start_dt = _parse_date(start)
    end_dt = _parse_date(end)
    if start_dt > end_dt:
        raise ValueError('Start date must be <= end date')
    filtered: List[Dict[str, Any]] = []
    for rec in data:
        rec_date = _parse_date(rec['date'])
        if start_dt <= rec_date <= end_dt:
            filtered.append(rec)
    return filtered

def aggregate_line(data: Iterable[Dict[str, Any]]) -> List[Tuple[date, float]]:
    """
    Aggregate data for a line chart: sum of values per day.

    Parameters
    ----------
    data : Iterable[Dict[str, Any]]
        The dataset to aggregate.

    Returns
    -------
    List[Tuple[date, float]]
        Sorted list of (date, aggregated_value) tuples.
    """
    totals: Dict[date, float] = {}
    for rec in data:
        d = _parse_date(rec['date']).date()
        totals[d] = totals.get(d, 0.0) + float(rec['value'])
    return sorted(totals.items())

def aggregate_bar(data: Iterable[Dict[str, Any]]) -> Dict[str, float]:
    """
    Aggregate data for a bar chart: sum of values per category.

    Records must contain a ``category`` key.  If missing, the record is
    ignored.

    Parameters
    ----------
    data : Iterable[Dict[str, Any]]
        The dataset to aggregate.

    Returns
    -------
    Dict[str, float]
        Mapping from category to aggregated value.
    """
    totals: Dict[str, float] = {}
    for rec in data:
        category = rec.get('category')
        if category is None:
            continue
        totals[category] = totals.get(category, 0.0) + float(rec['value'])
    return totals

def aggregate_donut(data: Iterable[Dict[str, Any]]) -> Dict[str, float]:
    """
    Aggregate data for a donut chart: same as bar chart but returns a
    dictionary suitable for percentage calculations.

    Parameters
    ----------
    data : Iterable[Dict[str, Any]]
        The dataset to aggregate.

    Returns
    -------
    Dict[str, float]
        Mapping from category to aggregated value.
    """
    return aggregate_bar(data)
