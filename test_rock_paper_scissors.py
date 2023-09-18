import unittest.mock
from rock_paper_scissors import get_name, validate_name, clear_screen, print_typewriter


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
