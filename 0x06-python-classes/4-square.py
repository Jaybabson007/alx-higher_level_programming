#!/usr/bin/python3
"""This defines a class Square."""


class Square:
     """This represents a square"""

    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """This function is used to Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This function returns the current area of the square."""
        return (self.__size * self.__size)
