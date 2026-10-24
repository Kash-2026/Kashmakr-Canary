import pytest
from model import generate_hashtags


def test_generate_hashtags():
    text = "This is a test text for generating hashtags. Hashtags are fun!"
    hashtags = generate_hashtags(text)
    assert len(hashtags) == 5
    assert "#hashtags" in hashtags
    assert "#test" in hashtags
    assert "#fun" in hashtags


def test_generate_hashtags_with_fewer_words():
    text = "few words"
    hashtags = generate_hashtags(text)
    assert len(hashtags) == 2
    assert "#few" in hashtags
    assert "#words" in hashtags


def test_generate_hashtags_with_no_words():
    text = ""
    hashtags = generate_hashtags(text)
    assert len(hashtags) == 0
