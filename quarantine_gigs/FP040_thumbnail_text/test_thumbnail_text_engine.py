import pytest
from thumbnail_text_engine import (
    generate_thumbnail_text,
    calculate_contrast_score,
    score_hook_strength,
)


def test_generate_thumbnail_text_length():
    text = generate_thumbnail_text("This is a test video concept", max_chars=10)
    assert len(text) <= 10, "Generated text exceeds maximum character limit"


def test_generate_thumbnail_text_content():
    text = generate_thumbnail_text("This is a test video concept")
    assert "test" in text, "Generated text does not contain expected content"


def test_calculate_contrast_score():
    score = calculate_contrast_score("test text")
    assert score == 0.7, "Contrast score does not match expected value"


def test_score_hook_strength():
    strength = score_hook_strength("test text")
    assert strength == 0.8, "Hook strength score does not match expected value"


def test_generate_thumbnail_text_min_contrast():
    with pytest.raises(ValueError):
        generate_thumbnail_text("low contrast", min_contrast=0.8)


def test_generate_thumbnail_text_empty_input():
    with pytest.raises(ValueError):
        generate_thumbnail_text("")


def test_generate_thumbnail_text_special_characters():
    text = generate_thumbnail_text("video!@#$%^&*()")
    assert text == "video", "Generated text contains unexpected characters"
