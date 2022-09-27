#!/usr/bin/python3
"""A function that returns the string representation of an obj"""
import json


def to_json_string(my_obj):
    """return the string represenatation of my_obj"""
    return json.dumps(my_obj)
