#!/usr/bin/python3
"""This script defines a class called Square.

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class.

    Args:
        Rectangle (Rectangle): the rectangle
    """

    def __init__(self, size):
        """This function creates new instances of class Square.

        Args:
            size (int): The size of 1 side of square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """This function returns a string representation of the square.

        Returns:
            str: A square.
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """This function calculates the area of a square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2
