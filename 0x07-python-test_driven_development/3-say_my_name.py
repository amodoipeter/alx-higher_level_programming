#!/usr/bin/python3

"""
This module contains the say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    The following returns first and last names.
    It prints an error message if a and b are
    not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
