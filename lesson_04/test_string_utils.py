import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    (" Hello world", "Hello world"),
    ("   python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol", [
    ("positive", "i"),
    (" Hello world", "world"),
    ("12345python", "12"),
])
def test_contains_positive(input_str, input_symbol):
    assert string_utils.contains(input_str, input_symbol)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ("positive", "c"),
    ("Hello world", "cat"),
    ("   ", "4"),
])
def test_contains_negative(input_str, input_symbol):
    assert string_utils.contains(input_str, input_symbol) is False


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("positive", "i", "postve"),
    (" Hello world", "world", " Hello "),
    ("12345python", "12", "345python"),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("positive", "c", "positive"),
    ("Hello world", "cat", "Hello world"),
    ("   ", "4", "   "),
])
def test_delete_symbol_negative(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected
