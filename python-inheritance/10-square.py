#!/usr/bin/python3
'''Module contains class Square that inherits from Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class defines a Square from Rectangle"""
    def __init__(self, size):
        """Initializes square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns area"""
        return super().area()# super() returns a proxy object representing the parent's class
