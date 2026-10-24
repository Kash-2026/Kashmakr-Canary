import random

THESIS_PLACEHOLDER = "THESIS"
HOOK_TYPES = ["anecdote", "question", "quote", "statistic"]


def generate_introduction(topic: str, hook_type: str) -> str:
    if hook_type not in HOOK_TYPES:
        raise ValueError("Invalid hook type")

    hooks = {
        "anecdote": f"Once upon a time, in the world of {topic}, THESIS.",
        "question": f"Have you ever wondered about {topic}? THESIS.",
        "quote": f"As someone wisely said, 'In the realm of {topic}, THESIS.'",
        "statistic": f"Did you know that {topic} impacts over X people? THESIS.",
    }

    introduction = hooks[hook_type].replace(
        THESIS_PLACEHOLDER, f"Here's your thesis on {topic}."
    )
    return introduction


def score_clarity(introduction: str) -> int:
    words = introduction.split()
    score = len(words) // 10
    return max(1, score)


def score_promise(introduction: str) -> int:
    thesis_present = THESIS_PLACEHOLDER.lower() in introduction.lower()
    return 10 if thesis_present else 1


def evaluate_introduction(introduction: str) -> dict:
    clarity_score = score_clarity(introduction)
    promise_score = score_promise(introduction)
    return {"clarity": clarity_score, "promise": promise_score}
