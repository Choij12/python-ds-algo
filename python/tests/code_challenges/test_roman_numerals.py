import pytest
from code_challenges.roman_numerals import roman_numeral

def test1():
    numerals = 'I'
    actual = roman_numeral(numerals)
    expected = 1
    assert actual == expected

def test2():
    numerals = 'V'
    actual = roman_numeral(numerals)
    expected = 5
    assert actual == expected

def test3():
    numerals = 'X'
    actual = roman_numeral(numerals)
    expected = 10
    assert actual == expected

def test4():
    numerals = 'L'
    actual = roman_numeral(numerals)
    expected = 50
    assert actual == expected

def test5():
    numerals = 'C'
    actual = roman_numeral(numerals)
    expected = 100
    assert actual == expected

def test6():
    numerals = 'D'
    actual = roman_numeral(numerals)
    expected = 500
    assert actual == expected

def test7():
    numerals = 'M'
    actual = roman_numeral(numerals)
    expected = 1000
    assert actual == expected
