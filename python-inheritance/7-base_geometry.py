#!/usr/bin/python3
'''Module contains class BaseGeometry'''


class BaseGeometry:
    """
    Class contains functions performing geometry based tasks
    """

    def area(self):

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
