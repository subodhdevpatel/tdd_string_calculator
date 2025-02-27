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


def test_multiple_numbers():
    calc = StringCalculator()
    assert calc.add("1,2") == 3
    assert calc.add("4,5,6") == 15


def test_newline_as_delimiter():
    calc = StringCalculator()
    assert calc.add("1\n2,3") == 6
    assert calc.add("4\n5\n6") == 15


def test_custom_delimiter():
    calc = StringCalculator()
    assert calc.add("//;\n1;2") == 3
    assert calc.add("//|\n2|3|4") == 9


def test_negative_numbers_throw_exception():
    calc = StringCalculator()
    with pytest.raises(ValueError, match="Negatives not allowed: .*"):
        calc.add("1,-2,3")


def test_ignore_numbers_greater_than_1000():
    calc = StringCalculator()
    assert calc.add("2,1001") == 2
    assert calc.add("1000,2") == 1002


def test_multi_character_custom_delimiter():
    calc = StringCalculator()
    assert calc.add("//[***]\n1***2***3") == 6


def test_multiple_custom_delimiters():
    calc = StringCalculator()
    assert calc.add("//[*][%]\n1*2%3") == 6
    assert calc.add("//[###][%%%]\n4###5%%%6") == 15


def test_trailing_delimiter():
    calc = StringCalculator()
    assert calc.add("1,2,\n") == 3  # Should handle gracefully
