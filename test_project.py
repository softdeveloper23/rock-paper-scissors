import unittest.mock
from project import (
    get_name,
    validate_name,
    get_difficulty,
    generate_random_move,
)

MOVES = ["rock", "paper", "scissors"]


def test_get_name():
    with unittest.mock.patch("project.input", return_value="John"), unittest.mock.patch(
        "project.validate_name", return_value=True
    ), unittest.mock.patch("project.clear_screen"), unittest.mock.patch(
        "project.print_typewriter"
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
    with unittest.mock.patch("project.input", return_value="easy"):
        assert get_difficulty() == "easy"

    with unittest.mock.patch("project.input", return_value="medium"):
        assert get_difficulty() == "medium"

    with unittest.mock.patch("project.input", return_value="hard"):
        assert get_difficulty() == "hard"

    # Test invalid input handling
    with unittest.mock.patch("project.input", side_effect=["invalid", "easy"]):
        assert get_difficulty() == "easy"


def test_generate_random_move_easy():
    with unittest.mock.patch("random.choice", return_value="rock"):
        result = generate_random_move(MOVES, "easy", [])
        assert result == "rock"


def test_generate_random_move_medium():
    with unittest.mock.patch("project.generate_medium_move", return_value="paper"):
        result = generate_random_move(MOVES, "medium", [])
        assert result == "paper"


def test_generate_random_move_hard():
    with unittest.mock.patch("project.generate_hard_move", return_value="scissors"):
        result = generate_random_move(MOVES, "hard", [])
        assert result == "scissors"
