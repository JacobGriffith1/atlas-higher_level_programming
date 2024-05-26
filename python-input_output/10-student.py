#!/usr/bin/python3
'''Module contains class Student'''


class Student:
    """Creates student instances"""

    def __init__(self, first_name, last_name, age):
        """Initialise instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict description"""
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for i in attrs:
                if type(i) is not str:
                    return obj

            dd = {}

            for i_attr in range(len(attrs)):
                for str_attr in obj:
                    if attrs[i_attr] == str_attr:
                        dd[str_attr] = obj[str_attr]
            return dd

        return obj
