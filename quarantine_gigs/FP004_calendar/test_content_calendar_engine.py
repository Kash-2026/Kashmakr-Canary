from content_calendar_engine import generate_calendar, score_channel_mix

def test_deterministic_calendar_generation():
    cal1 = generate_calendar("SaaS Marketing")
    cal2 = generate_calendar("SaaS Marketing")
    assert cal1 == cal2
    assert len(cal1) == 30
    assert cal1[0]["day"] == 1
    assert "channel" in cal1[0]

def test_score_channel_mix():
    cal = generate_calendar("Fintech")
    mix = score_channel_mix(cal)
    assert sum(mix.values()) > 0.95
    assert "Twitter" in mix or "LinkedIn" in mix
