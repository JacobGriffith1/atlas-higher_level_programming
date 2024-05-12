#!/usr/bin/python3
"""Module contains class Square, which defines a square object by its size"""


class Square:
    """Class Square defines a square by its size"""
    def __init__(self, size=0):
        """Method to initialize the square

            Args:
                __size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
