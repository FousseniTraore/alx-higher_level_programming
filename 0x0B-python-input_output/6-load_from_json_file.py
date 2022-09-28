#!/usr/bin/python3
"""Function that create an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Doc"""
    with open(filename, "w") as f:
        return json.load(f)
