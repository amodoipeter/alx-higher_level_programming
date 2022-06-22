#!/usr/bin/python3
"""Class Square defines a square"""


class Square:
    """This class defines a square.

      This class has no public attributes.

      """
    def __init__(self, size=0, position=(0, 0)):
        """This method initiates a square.

             Args:
                 size (int): This defines the size of the square.
                     The size is validated in the setter method.
                 position (tuple): This defines the position of the square.
                     The position is validated in the setter method

             """
        self.size = size
        self.position = position

    def area(self):
        """int: Return area of square."""
        return self.__size**2

    @property
    def size(self):
        """This method retrieves the size of a square."""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size of a square.

                Args:
                    size (int): This defines the size of the square.
                        The size is validated with try/except."""

        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """This method retrieves the position of a square."""
        return self.__position

    @position.setter
    def position(self, value):
        """This method sets the position of a square

              Args:
                  position: this tuple defines the position of the square.
                      The position is validated with try/except.

              """
        self.__position = value
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__position[1]):
                print("")
            for y in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
