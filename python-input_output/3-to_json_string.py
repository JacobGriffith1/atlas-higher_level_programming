#!/usr/bin/python3
'''Module contains function to_json_string'''
import json


def to_json_string(my_obj):
    """
    Function returns the JSON representation of an object (string)

    Args:
        my_obj: object

    Exception:
        Exception: object can't be encoded
    """

    return json.dumps(my_obj)
