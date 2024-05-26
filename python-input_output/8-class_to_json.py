#!/usr/bin/python3
'''Module contains function class_to_json'''


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    """

    dd = {}
    if hasattr(obj, "__dict__"):
        dd = obj.__dict__.copy()
    return dd
