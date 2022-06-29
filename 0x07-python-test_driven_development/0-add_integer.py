#!/usr/bin/python3

"""
function that adds two integers
"""


def add_integer(a, b=98):
    """
    return sum of a and b. print an error message if a and b aren't integers or floats
    :param a:
    :param b:
    :return:
    """
    if type(a) == float:
        a = int(a)
    elif type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) == float:
        b = int(b)
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
