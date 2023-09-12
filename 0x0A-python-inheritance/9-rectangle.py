#!/usr/bin/python3
"""This python script defines a class called rectangle 

Attributes:
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """This function creates new instances of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """This function calculates the area of a rectangle.

        Returns:
            int: the area.
        """
        return self.__width * self.__height

    def __str__(self):
        """This function returns a string representation of the rectangle.

        Returns:
            str: A string representation of rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
