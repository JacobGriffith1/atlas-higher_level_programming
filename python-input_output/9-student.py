#!/usr/bin/python3
'''Module contains class Student'''


class Student:
    """Creates student instances"""

    def __init__(self, first_name, last_name, age):
        """Initialise instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dict description"""
        return self.__dict__.copy()
