#!/usr/bin/python3
"""object instance of a class that inherited (directly or indirectly) from class
"""


def inherits_from(obj, a_class):
    """loop through to check if object is a subclass of a_class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
