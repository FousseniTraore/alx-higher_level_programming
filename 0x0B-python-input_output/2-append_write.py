#!/usr/bin/python3
"""Function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Doc"""
    with open(filename, "a", encoding="utf-8"):
        return (f.write(text))
