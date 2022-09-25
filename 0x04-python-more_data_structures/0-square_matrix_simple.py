#!/usr/bin/python3
""" A function that return the sqaure of each element in a matrix"""


def square_matrix_simple(matrix=[]):
    """This function create a matrix usinf a sqaure of all the element of an input matrix"""
    return ([list(map(lambda x: x * x, row)) for row in matrix])