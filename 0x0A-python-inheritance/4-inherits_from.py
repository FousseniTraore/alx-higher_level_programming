#!/usr/bin/python3
"""Doc"""


def inherits_from(obj, a_class):
    """Doc"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
