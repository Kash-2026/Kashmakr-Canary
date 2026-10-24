"""Deterministic Social Content Calendar Engine in Python 3.12."""
import hashlib
from datetime import datetime, timedelta

def generate_calendar(niche: str, cadence: int = 1, weights: dict = None) -> list:
    """Generate a deterministic 30-day schedule."""
    if not weights:
        weights = {"educational": 0.4, "promotional": 0.3, "behind_the_scenes": 0.3}
    
    channels = ["Twitter", "LinkedIn", "Instagram"]
    schedule = []
    base_date = datetime(2026, 1, 1)
    
    categories = sorted(list(weights.keys()))
    
    for day in range(30):
        date_str = (base_date + timedelta(days=day)).strftime("%Y-%m-%d")
        # Deterministic hash selection based on niche and day
        seed_int = int(hashlib.sha256(f"{niche}_{day}".encode()).hexdigest(), 16)
        cat = categories[seed_int % len(categories)]
        channel = channels[(seed_int >> 4) % len(channels)]
        
        topic = f"{niche.title()} - {cat.replace('_', ' ').title()} Strategy Day {day + 1}"
        schedule.append({
            "day": day + 1,
            "date": date_str,
            "channel": channel,
            "category": cat,
            "topic": topic
        })
    return schedule

def score_channel_mix(schedule: list) -> dict:
    """Computes distribution across channels."""
    if not schedule:
        return {}
    mix = {}
    for item in schedule:
        c = item.get("channel", "Unknown")
        mix[c] = mix.get(c, 0) + 1
    total = len(schedule)
    return {c: round(count / total, 2) for c, count in mix.items()}


generate_content_calendar = generate_calendar
