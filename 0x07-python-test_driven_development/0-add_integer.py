#!/usr/bin/python3
"""This is the 0-add_interger.py file"""


def add_integer(a, b=98):
    """The function that add the integer a and b"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
