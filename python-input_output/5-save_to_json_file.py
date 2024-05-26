#!/usr/bin/python3
'''Module contains function save_to_json_file'''
import json


def save_to_json_file(my_obj, filename):
    """
    Function writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: object
        filename: file name

    Raises:
        Exception: object can't be encoded
    """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
