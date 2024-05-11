#!/usr/bin/python3
"""Module contains class Square that defines a square by its size"""


class Square:
    """Class Square defines a square by its size"""
    def __init__(self, size=0, position=(0, 0)):
        """Method to initialize the square"""
        self.size = size
        self.position = position

    def area(self):
        """Method that returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Method that prints the square in stdout using #"""
        if not self.__size:
            print()
        else:
            for x in range(self.position[1]):
                print()
            for x in range(self.__size):
                for i in range(self.position[0]):
                    print(" ", end='')
                for y in range(self.__size):
                    print("#", end='')
                print()

    @property
    def size(self):
        """Method to return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the size value of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Method that returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Method to set the value of the position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
