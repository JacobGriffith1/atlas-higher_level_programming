#!/usr/bin/python3
'''Module contains class Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that defines a rectangle from BaseGeometry class"""

    def __init__(self, width, height):
        """Initializes an instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """Returns area of instance"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the printable string"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
