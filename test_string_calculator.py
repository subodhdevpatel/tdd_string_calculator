import pytest
from string_calculator import StringCalculator


def test_empty_string_returns_zero():
    calc = StringCalculator()
    assert calc.add("") == 0


def test_none_returns_zero():
    calc = StringCalculator()
    assert calc.add(None) == 0
