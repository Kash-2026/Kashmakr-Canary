"""Model"""

import csv
from pathlib import Path
from typing import List, Sequence


def _parse_alignment(alignment: str, ncols: int) -> List[str]:
    """Return a list of alignment specifiers for each column."""
    if not alignment:
        return ["l"] * ncols
    # Pad or truncate alignment string to match number of columns
    if len(alignment) < ncols:
        alignment = alignment + alignment[-1] * (ncols - len(alignment))
    else:
        alignment = alignment[:ncols]
    # Normalize to lowercase
    return [c.lower() for c in alignment]


def _build_separator(width: int, align: str) -> str:
    """Return the markdown separator for a column."""
    if align == "r":
        return "-" * (width - 1) + ":"
    if align == "c":
        return ":" + "-" * (width - 2) + ":"
    # left or any other value defaults to left alignment
    return "-" * width


def _pad_cell(cell: str, width: int, align: str) -> str:
    """Pad a cell according to the alignment."""
    if align == "r":
        return cell.rjust(width)
    if align == "c":
        return cell.center(width)
    # left or any other value defaults to left alignment
    return cell.ljust(width)


def _wrap_text(text: str, width: int) -> str:
    """Wrap text to specified width."""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 > width:
            lines.append(current_line)
            current_line = word
        else:
            if current_line:
                current_line += " "
            current_line += word
    if current_line:
        lines.append(current_line)
    return "\n".join(lines)


def csv2md(
    csv_file: str | Path,
    *,
    alignment: str = "",
    max_width: int | None = None,
) -> str:
    """
    Convert a CSV file to a Markdown table string.

    Parameters
    ----------
    csv_file : str | Path
        Path to the CSV file.
    alignment : str, optional
        Alignment specification per column. Each character corresponds to a column:
        'l' (left), 'r' (right), 'c' (center). If fewer characters than columns,
        the last character is repeated. Default is left alignment for all columns.
    max_width : int, optional
        Maximum width for a column. If set, long values are wrapped at this width.

    Returns
    -------
    str
        Markdown table representation of the CSV.
    """
    path = Path(csv_file)
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        return ""

    headers = rows[0]
    data_rows = rows[1:]

    ncols = len(headers)
    alignments = _parse_alignment(alignment, ncols)

    # Compute column widths
    col_widths = [len(h) for h in headers]
    for row in data_rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(cell))

    if max_width:
        for i, col_width in enumerate(col_widths):
            if col_width > max_width:
                col_widths[i] = max_width

    # Build header row
    header_cells = [h.ljust(col_widths[i]) for i, h in enumerate(headers)]
    header_line = "|" + "|".join(header_cells) + "|"

    # Build separator row
    sep_cells = [
        _build_separator(col_widths[i], alignments[i]) for i in range(ncols)
    ]
    sep_line = "|" + "|".join(sep_cells) + "|"

    # Build data rows
    data_lines = []
    for row in data_rows:
        line_cells = []
        for i, cell in enumerate(row):
            # Escape pipe characters
            cell = cell.replace("|", r"\|")
            if max_width and len(cell) > max_width:
                cell = _wrap_text(cell, max_width)
            padded = _pad_cell(cell, col_widths[i], alignments[i])
            line_cells.append(padded)
        data_lines.append("|" + "|".join(line_cells) + "|")

    # Assemble final table
    table = "\n".join([header_line, sep_line] + data_lines) + "\n"
    return table