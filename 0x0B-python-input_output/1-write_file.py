#!/usr/bin/python3
"""A function that write a string to a file"""


def write_file(filename="", text=""):
    """Doc"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
