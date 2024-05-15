#!/usr/bin/python3
"""
Module contains function that prints a square of '#'
"""


def print_square(size):
    """Function prints a square of '#'
    
    Args:
        size: size of the square to print

    Return:
        N/A
    
    Raises:
        TypeError: Size is not an int
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be  >= 0")
    
    for i in range(size):
        print("#" * size)