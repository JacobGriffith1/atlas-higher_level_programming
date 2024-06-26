#!/usr/bin/python3
"""Module contains class: Square; which inherits from class: Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class: Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override of __str__ builtin"""
        str_Square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}".format(self.width)

        return str_Square + str_id + str_xy + str_wh

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args is not None and len(args) is not 0:
            listAttr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if listAttr[i] == 'size':
                    setattr(self, 'width', args[1])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, listAttr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        listAttr = ['id', 'size', 'x', 'y']
        dictionary = {}

        for key in listAttr:
            if key == 'size':
                dictionary[key] = getattr(self, 'width')
            else:
                dictionary[key] = getattr(self, key)

        return dictionary
