#!/usr/bin/python3
"""Module contains class Rectangle"""


class Rectangle:
    """Class defining a Rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initializes rectangle instance
        
        Args:
            self.width = width
            self.height = height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method returns width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """method sets width value

        Args:
            value: width

        Raises:
            TypeError: width =! an integer
            ValueError: width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method returns height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """method sets height value
        
        Args:
            value: height

        Raises:
            TypeError: height != an integer
            ValueError: height < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
