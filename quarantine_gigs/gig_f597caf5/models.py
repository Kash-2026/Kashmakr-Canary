import math
from typing import Any, Dict, Iterable, List, Optional


def analyze_competitors(competitors: Optional[Iterable[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    """
    Analyze a collection of competitor data dictionaries.

    Parameters
    ----------
    competitors : Iterable[Dict[str, Any]] | None
        An iterable of competitor records. Each record should contain the keys
        ``name``, ``marketShare``, ``strengths`` and ``weaknesses``. The
        ``marketShare`` value may be a string ending with a percent sign (e.g.
        ``"25%"``) or a numeric value. If ``competitors`` is ``None`` or not
        iterable, an empty list is returned.

    Returns
    -------
    List[Dict[str, Any]]
        A list of dictionaries with the following keys:

        - ``name``: the competitor's name.
        - ``market_share``: the market share as a float (e.g. 25.0 for 25%).
        - ``strengths``: the original strengths value.
        - ``weaknesses``: the original weaknesses value.

    Notes
    -----
    The function is defensive: it does not raise an exception if the input is
    malformed. Missing keys are replaced with ``None`` and percent strings are
    parsed safely.
    """
    # Defensive check: if input is None or not iterable, return empty list
    if not isinstance(competitors, Iterable):
        return []

    analysis: List[Dict[str, Any]] = []

    for competitor in competitors:
        # Ensure we have a mapping; skip non-dict items
        if not isinstance(competitor, dict):
            continue

        # Extract fields with defaults
        name = competitor.get("name")
        market_share_raw = competitor.get("marketShare")
        strengths = competitor.get("strengths")
        weaknesses = competitor.get("weaknesses")

        # Parse market share: accept numeric or string with %
        try:
            if isinstance(market_share_raw, str):
                market_share = float(market_share_raw.strip("%"))
            else:
                market_share = float(market_share_raw)
        except (TypeError, ValueError):
            market_share = None

        analysis.append(
            {
                "name": name,
                "market_share": market_share,
                "strengths": strengths,
                "weaknesses": weaknesses,
            }
        )

    return analysis