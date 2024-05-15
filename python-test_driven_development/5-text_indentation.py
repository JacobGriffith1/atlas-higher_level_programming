#!/usr/bin/python3
"""
Module contains a function that prints text with 2 nl after certain chars
"""


def text_indentation(text):
    """Function prints a message and newlines after certain chars

    Args:
        text: Text to print

    Returns:
        N/A

    Raises:
        TypeError: Text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    t = text[:]

    for c in ".?:":
        list = t.split(c)
        t = ""
        for p in list:
            p = p.strip(" ")
            t = p + c if t is "" else t + "\n\n" + p + c

    print(t[:-3], end=""),
