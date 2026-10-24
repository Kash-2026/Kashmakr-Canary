import math
from typing import List, Dict


def project_growth(
    upload_cadence: int,
    topic_mix: float,
    retention_rate: float,
    initial_subscribers: int,
    months: int,
) -> List[int]:
    """
    Projects subscriber growth based on upload cadence, topic mix, retention rate, and initial subscribers.

    Parameters:
    upload_cadence (int): Number of uploads per month.
    topic_mix (float): Proportion of high-engagement topics (0 to 1).
    retention_rate (float): Monthly retention rate (0 to 1).
    initial_subscribers (int): Initial number of subscribers.
    months (int): Number of months to project.

    Returns:
    List[int]: List of subscriber counts for each month.
    """
    if months <= 0:
        return []

    subscribers = [initial_subscribers]
    for _ in range(months):
        # Gain is a fixed monthly lift from uploads, retention-weighted.
        # With uploads active there is no compounding churn; without
        # uploads the list decays purely by the retention rate.
        if upload_cadence > 0:
            new_subscribers = upload_cadence * 100 * retention_rate
            subscribers.append(subscribers[-1] + new_subscribers)
        else:
            subscribers.append(subscribers[-1] * retention_rate)
    return [int(round(sub)) for sub in subscribers]


def milestone_checkpoints(
    subscribers: List[int], milestones: List[int]
) -> Dict[int, int]:
    """
    Identifies when subscriber milestones are reached.

    Parameters:
    subscribers (List[int]): List of subscriber counts for each month.
    milestones (List[int]): List of milestone subscriber counts.

    Returns:
    Dict[int, int]: Dictionary with milestones as keys and the month (1-indexed) they are reached as values.
    """
    if not milestones:
        return {}

    checkpoints: Dict[int, int] = {}
    for milestone in milestones:
        reached_at = None
        for i, sub in enumerate(subscribers):
            if sub >= milestone:
                reached_at = i
                break
        if reached_at is None:
            # milestone never reached within the projection window
            continue
        # month index: a milestone reached at subscribers[0] is month 0;
        # otherwise it is one less than the 0-based index where it crossed.
        checkpoints[milestone] = max(0, reached_at - 1)
    return checkpoints