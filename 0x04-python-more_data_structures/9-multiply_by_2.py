#!/usr/bin/python3
"""a function that returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    """Doc"""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
