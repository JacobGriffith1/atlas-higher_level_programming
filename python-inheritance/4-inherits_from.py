#!/usr/bin/python3
'''Module contains inherits_from function'''


def inherits_from(obj, a_class):
    """
    Function returns 'True' if the object is an instance of a
    class that inherited (directly or indirectly) from the
    specified class; otherwise 'False'

    Args:
        obj: Object parameter
        a_class: Class parameter

    Return:
        True if object issubclass of a_class, else False
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        # issubclass returns whether a class is derived
        # from another class or is the same class
        return True
    else:
        return False
