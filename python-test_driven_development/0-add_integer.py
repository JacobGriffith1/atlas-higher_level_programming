#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Function adds two integer/floating numbers.

    Args:
        a: First number variable
        b: Second number variable

    Returns:
        The sum of the given numbers

    Raises:
        TypeError: Variable(s) a and b are not integers/floats
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
