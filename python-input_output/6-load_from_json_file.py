#!/usr/bin/python3
'''Module contains function load_from_json_file'''
import json


def load_from_json_file(filename):
    """
    Function creates an Object from a "JSON file"

    Args:
        filename: textfile name

    Raises:
        Exception: object can't be encoded
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
