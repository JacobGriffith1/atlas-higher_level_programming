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
        list = s.split(c)
        s = ""
        for l in list:
            l = l.strip(" ")
            s = i + c if s is "" else s + "\n\n" + l + c

    print(s[:-3], end=""),
