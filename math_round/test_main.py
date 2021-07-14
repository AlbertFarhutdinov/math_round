"""This module contain test for `math_round` project."""


import pytest

from .main import get_rounded_number


CASES = {
    0: [
        (0.0, 0.0),
        (0.1, 0.0),
        (0.4, 0.0),
        (0.5, 1.0),
        (0.6, 1.0),
        (0.9, 1.0),
        (1.0, 1.0),
        (1.1, 1.0),
        (-0.0, 0.0),
        (-0.1, 0.0),
        (-0.4, 0.0),
        (-0.5, -1.0),
        (-0.6, -1.0),
        (-0.9, -1.0),
        (-1.0, -1.0),
        (-1.1, -1.0),
    ],
    1: [
        (0.00, 0.0),
        (0.01, 0.0),
        (0.04, 0.0),
        (0.05, 0.1),
        (0.06, 0.1),
        (0.09, 0.1),
        (0.10, 0.1),
        (0.11, 0.1),
        (-0.00, 0.0),
        (-0.01, 0.0),
        (-0.04, 0.0),
        (-0.05, -0.1),
        (-0.06, -0.1),
        (-0.09, -0.1),
        (-0.10, -0.1),
        (-0.11, -0.1),
    ]
}


@pytest.mark.parametrize("number, expected", CASES[0])
def test_get_rounded_number_0(number, expected):
    """
    Test for `get_rounded_number` with `number_of_digits_after_separator`
    equal to 0.

    """
    assert get_rounded_number(number, 0) == expected


@pytest.mark.parametrize("number, expected", CASES[1])
def test_get_rounded_number_1(number, expected):
    """
    Test for `get_rounded_number` with `number_of_digits_after_separator`
    equal to 1.

    """
    assert get_rounded_number(number, 1) == expected
