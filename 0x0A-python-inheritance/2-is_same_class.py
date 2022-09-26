#!/usr/bin/python3
"""Return True if object is an instance of the specified class"""


def is_same_class(obj, a_class):
    """Verify if the type of the object is equal to a_class"""
    if type(obj) == a_class:
        return True
    else:
        return False