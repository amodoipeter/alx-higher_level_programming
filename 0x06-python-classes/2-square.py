#!/usr/bin/python3
"""Class Square defines a square"""

class Square:
    """This class defines a square.

        This class has no public attributes.

        """
    def __init__(self, size=0):
        """This method initiates a square.

               Args:
                   size (int): This defines the size of the square.
                       The size is validated with try/except.

               """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
