#!/usr/bin/python3
'''Module contains function read_file'''


def read_file(filename=""):
    """
    Function reads text file (UTF8) and prints it to stdout
    
    Args:
        filename: file name
    
    Raises:
        Exception: file can be opened
    """

with open(filename, 'r', encoding="utf-8") as f:
    data = f.read()
    print(data, end='')
