#!/usr/bin/python3
'''Module contains function from_json_string'''
import json


def from_json_string(my_str):
    """
    Function returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: JSON representation

    Raises:
        Exception: string can't be decoded
    """

    return json.loads(my_str)
