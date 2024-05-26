#!/usr/bin/python3
'''Module contains function write_file'''


def write_file(filename="", text=""):
    """
    Function writes text to a file

    Args:
        filename: file name
        text: text to write

    Raises
        Exception: file can be opened
    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
