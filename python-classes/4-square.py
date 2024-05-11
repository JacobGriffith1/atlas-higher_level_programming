#!/usr/bin/python3
"""Module contains class Square that defines a square by its size"""


class Square:
    """Class Square defines a square by its size"""
    def __init__(self, size=0):
        """Method to initialize the square's size

        Args:
            __size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method that returns the area of the square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Method to return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size value of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
