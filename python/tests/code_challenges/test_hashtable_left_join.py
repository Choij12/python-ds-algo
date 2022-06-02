import pytest
from code_challenges.hashtable_left_join import left_join

def test_exists():
    assert left_join

def test_left_join():
    synonyms = {'happy': 'joy'}

    antonyms = {'happy': 'mad'}

    assert left_join(synonyms, antonyms) == ['happy', 'joy', 'mad']

def test_left_join1():
    synonyms = {'happy': 'joy','scared':'afraid'}

    antonyms = {'happy': 'mad','scared':'brave'}

    assert left_join(synonyms, antonyms) == ['happy', 'joy', 'mad',
                                             'scared', 'afraid', 'brave']

def test_left_join_with_none():
    synonyms = {'happy': 'joy','scared':'afraid','sad':'cry'}

    antonyms = {'happy': 'mad','scared':'brave'}

    assert left_join(synonyms, antonyms) == ['happy', 'joy', 'mad',
                                             'scared', 'afraid', 'brave',
                                             'sad', 'cry', None]
