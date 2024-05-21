#!/usr/bin/python3
'''Module contains is_kind_of_class function'''


def is_kind_of_class(obj, a_class):
    """
    Function returns 'True' if the object is exactly an instance
    of the specified class OR an instance of a class that
    inherited from the specified class; otherwise 'False'

    Args:
        obj: An object to check the type of
        a_class: A class to compare obj to

    Return:
        True if obj isinstance of a_class
    """

    if isinstance(obj, a_class):
        # isinstance returns whether an object is an
        # instance of a class, or a subclass thereof
        return True
    else:
        return False
