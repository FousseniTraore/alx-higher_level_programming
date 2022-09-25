#!/usr/bin/python3
"""a function that adds all unique integers in a list"""


def uniq_add(my_list=[]):
    """add all uniq integer to a list"""
    result = 0
    for x in set(my_list):
        result += x
    return (result)
