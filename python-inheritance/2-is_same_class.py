#!/usr/bin/python3
'''Module contains is_same_class function'''


def is_same_class(obj, a_class):
    """
    Function returns 'True' if the object is exactly an instance
    of the specified class; otherwise 'False'

    Args:
        obj: An object to check the type of
        a_class: A class to compare obj to

    Return:
        True if obj isinstance of a_class
    """

    if type(obj) == a_class:
        # comparing types to determine if obj 
        # isinstance of a_class
        return True
    else:
        return False
