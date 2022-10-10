#!/usr/bin/python3
"""Doc"""


def safe_print_division(a, b):
    try:
        result = a / b
    except (ValueError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
