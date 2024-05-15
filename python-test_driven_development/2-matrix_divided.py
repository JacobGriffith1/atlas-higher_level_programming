#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function divides all elements of a matrix.

    Args:
        matrix: A matrix of integers and floats
        div: The divisor; either an integer or a float

    Returns:
        A new matrix of quotients

    Raises:
        TypeError: Elements of the matrix are not lists
                   Elements are not integers or floats
                   Div is not an integer or float
                   Lists of matrix are not the same size

        ZeroDivisionError: Div is zero
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    typeMsg = "matrix must be a matrix (list of lists) of integers/floats"
    sizeMsg = "Each row of the matrix must have the same size"
    length = 0

    for elem in matrix:
        if not elem or not isinstance(elem, list):
            raise TypeError(typeMsg)

        if length != 0 and len(elem) != length:
            raise TypeError(sizeMsg)

        for num in elem:
            if not type(num) in (int, float):
                raise TypeError(typeMsg)

        length = len(elem)

    q = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (q)
