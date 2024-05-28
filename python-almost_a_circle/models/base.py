#!/usr/bin/python3
"""Module contains class: Base"""
import json
import csv
import os.path


class Base:
    """Class: Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def check_int(value, val_name, min=None):
        """Check if an int value is valid, raise error if not"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(val_name))
        if min is None:
            if value <= 0:
                raise ValueError("{} must be > 0".format(val_name))
        else:
            if value < min:
                raise ValueError("{} must be >= {}".format(val_name, min))
        return value

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        listDict = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                listDict.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(listDict)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            new = cls(3, 5)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_string = f.read()

        list_class = cls.from_json_string(list_string)
        list_instance = []

        for i in range(len(list_class)):
            list_instance.append(cls.create(**list_class[i]))

        return list_instance
