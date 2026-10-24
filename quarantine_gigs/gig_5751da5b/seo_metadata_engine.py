import re

class SEOMetadataEngine:
    MAX_TITLE_PIXELS = 600
    MAX_DESCRIPTION_CHARACTERS = 160

    def __init__(self, page_topic, keyword):
        self.page_topic = page_topic
        self.keyword = keyword

    def generate_title(self):
        title = f"{self.keyword} | {self.page_topic}"
        return self._check_pixel_limit(title, self.MAX_TITLE_PIXELS)

    def generate_description(self):
        description = (
            f"Learn more about {self.page_topic} and how {self.keyword} can help."
        )
        return self._check_character_limit(description, self.MAX_DESCRIPTION_CHARACTERS)

    def _check_pixel_limit(self, text, limit):
        pixel_length = sum([1 if ord(c) < 128 else 2 for c in text])
        return text[:limit] if pixel_length > limit else text

    def _check_character_limit(self, text, limit):
        return text[:limit] if len(text) > limit else text

    def check_keyword_placement(self, text):
        return self.keyword.lower() in text.lower()

    def score_click_through_potential(self, title, description):
        score = 0
        if self.check_keyword_placement(title):
            score += 1
        if self.check_keyword_placement(description):
            score += 1
        return score

# test_seo_metadata_engine.py
import pytest
from seo_metadata_engine import SEOMetadataEngine

def test_generate_title():
    engine = SEOMetadataEngine("Page Topic", "Keyword")
    title = engine.generate_title()
    assert "Keyword | Page Topic" in title
    assert len(title) <= engine.MAX_TITLE_PIXELS

def test_generate_description():
    engine = SEOMetadataEngine("Page Topic", "Keyword")
    description = engine.generate_description()
    assert "Learn more about Page Topic and how Keyword can help." in description
    assert len(description) <= engine.MAX_DESCRIPTION_CHARACTERS

def test_check_keyword_placement():
    engine = SEOMetadataEngine("Page Topic", "Keyword")
    assert engine.check_keyword_placement("Keyword is important")
    assert not engine.check_keyword_placement("No keyword here")

def test_score_click_through_potential():
    engine = SEOMetadataEngine("Page Topic", "Keyword")
    title = "Keyword | Page Topic"
    description = "Learn more about Page Topic and how Keyword can help."
    score = engine.score_click_through_potential(title, description)
    assert score == 2

def test_check_pixel_limit():
    engine = SEOMetadataEngine("Page Topic", "Keyword")
    long_text = "a" * 700
    limited_text = engine._check_pixel_limit(long_text, 600)
    assert len(limited_text) <= 600

def test_check_character_limit():
    engine = SEOMetadataEngine("Page Topic", "Keyword")
    long_text = "a" * 170
    limited_text = engine._check_character_limit(long_text, 160)
    assert len(limited_text) <= 160