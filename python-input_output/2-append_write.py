#!/usr/bin/python3
'''Module contains function append_write'''


def append_write(filename="", text=""):
    """
    Function appends text to a file

    Args:
        filename: file name
        text: text to write

    Raises:
        Exception: file can be opened
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
