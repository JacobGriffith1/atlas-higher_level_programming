#!/usr/bin/python3
'''Module contains lookup function'''


def lookup(obj):
    """
    Function returns the list of available
    attributes and methods of an object
    
    Args:
        obj: Instance of the class
    
    Return:
        List of attributes and methods of an object
    """

    return dir(obj)
    #dir builtin shows the attributes of an object
