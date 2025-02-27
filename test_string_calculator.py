import pytest
from string_calculator import StringCalculator


def test_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.add("") == 0


def test_none_returns_zero():
    calc = StringCalculator()
    assert calc.add(None) == 0


def test_single_number_returns_same_number():
    calc = StringCalculator()
    assert calc.add("5") == 5
    assert calc.add("15") == 15
