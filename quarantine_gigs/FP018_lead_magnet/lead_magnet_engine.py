import random

def generate_lead_magnet_concepts(audience, pain_point):
    concepts = [
        f"E-book: 'Overcoming {pain_point} for {audience}'",
        f"Webinar: 'How {audience} can solve {pain_point}'",
        f"Template: '{audience}-specific plan to tackle {pain_point}'",
        f"Video series: 'Step-by-step guide for {audience} to overcome {pain_point}'",
        f"Checklist: 'Essential tips for {audience} to handle {pain_point}'",
    ]
    return random.choice(concepts)

def get_format_delivery_choices():
    choices = [
        "PDF download",
        "Email series",
        "Webinar registration",
        "Video on-demand",
        "Interactive online tool",
    ]
    return random.choice(choices)

def calculate_conversion_likelihood(audience, pain_point):
    base_score = 50
    audience_factor = random.uniform(0.8, 1.2)
    pain_point_factor = random.uniform(0.8, 1.2)
    score = base_score * audience_factor * pain_point_factor
    return float(max(40.0, min(60.0, round(score, 2))))