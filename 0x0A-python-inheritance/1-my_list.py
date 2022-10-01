#!/usr/bin/python3
"""A class myList that inherits from list"""


class MyList(list):
    """Doc"""
    def print_sorted(self):
        """print a list in ascending order"""
        print(sorted(self))
