#!/usr/bin/python3
"""Doc"""


def append_after(filename="", search_string="", new_string=""):
    """Doc"""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
