import pytest
from logic_utils import check_guess


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
