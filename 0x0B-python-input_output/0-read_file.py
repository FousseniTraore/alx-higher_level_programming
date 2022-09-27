#!/usr/bin/python3
"""A function that read a text file usign with"""


def read_file(filename=""):
    """Doc"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
