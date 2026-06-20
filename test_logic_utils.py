import pytest
from logic_utils import check_guess, get_range_for_difficulty, parse_guess


def test_parse_guess():
    # valid integer
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

    # valid float string is truncated to int
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7
    assert err is None

    # None input
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

    # empty string
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

    # non-numeric string
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."

    # special characters
    ok, value, err = parse_guess("!@#")
    assert ok is False
    assert err == "That is not a number."


def test_get_range_for_difficulty():
    # known difficulties return correct ranges
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)

    # unknown difficulty falls back to (1, 100)
    assert get_range_for_difficulty("Unknown") == (1, 100)
    assert get_range_for_difficulty("") == (1, 100)


def test_check_guess():
    # correct guess
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"
    assert "Correct" in message

    # guess too high
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

    # guess too low
    outcome, message = check_guess(10, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

    # boundary: exact match at 1
    outcome, _ = check_guess(1, 1)
    assert outcome == "Win"

    # boundary: off by one high
    outcome, _ = check_guess(51, 50)
    assert outcome == "Too High"

    # boundary: off by one low
    outcome, _ = check_guess(49, 50)
    assert outcome == "Too Low"

    # incompatible types raise TypeError
    with pytest.raises(TypeError):
        check_guess(42, "fifty")
