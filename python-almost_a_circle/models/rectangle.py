#!/usr/bin/python3
"""Module contains class: Rectangle; which inherits from class: Base"""
from models.base import Base


class Rectangle(Base):
    """Class: Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Height setter"""
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        self.__y = value
