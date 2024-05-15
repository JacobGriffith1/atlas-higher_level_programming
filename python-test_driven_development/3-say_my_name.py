#!/usr/bin/python3
"""
This module contains a functon that prints a first/last name message
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first name> <last name>"
    
    Args:
        first_name: First name
        last_name: Last name

    Returns:
        N/A

    Raises:
        TypeError: Either variable is not a string
    """

if type(first_name) is not str:
    raise TypeError("first_name must be a string")

if type(last_name) is not str:
    raise TypeError("last_name must be a string")

print("My name is {} {}".format(first_name, lastname))