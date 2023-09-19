import unittest.mock
from rock_paper_scissors import get_name, validate_name, get_difficulty


def test_get_name():
    with unittest.mock.patch(
        "rock_paper_scissors.input", return_value="John"
    ), unittest.mock.patch(
        "rock_paper_scissors.validate_name", return_value=True
    ), unittest.mock.patch(
        "rock_paper_scissors.clear_screen"
    ), unittest.mock.patch(
        "rock_paper_scissors.print_typewriter"
    ):
        result = get_name()
        assert result == "John"


def test_validate_name():
    # Test valid names
    assert validate_name("John") is True
    assert validate_name("Jane") is True

    # Test invalid names
    assert validate_name("") is False
    assert validate_name("123") is False


def test_get_difficulty():
    # Test valid difficulty levels
    with unittest.mock.patch("rock_paper_scissors.input", return_value="easy"):
        assert get_difficulty() == "easy"

    with unittest.mock.patch("rock_paper_scissors.input", return_value="medium"):
        assert get_difficulty() == "medium"

    with unittest.mock.patch("rock_paper_scissors.input", return_value="hard"):
        assert get_difficulty() == "hard"

    # Test invalid input handling
    with unittest.mock.patch(
        "rock_paper_scissors.input", side_effect=["invalid", "easy"]
    ):
        assert get_difficulty() == "easy"
