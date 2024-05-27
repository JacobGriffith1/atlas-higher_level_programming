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
