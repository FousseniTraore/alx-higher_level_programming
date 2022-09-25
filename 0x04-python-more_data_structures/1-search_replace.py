#!/usr/bin/python3
"""Function that replaces an element by another"""


def search_replace(my_list, search, replace):
    """Replace search el by the replace el in the new list"""
    new_list = my_list
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return(new_list)
