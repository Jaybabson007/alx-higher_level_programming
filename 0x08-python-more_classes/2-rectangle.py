#!/usr/bin/python3
#2-rectangle.py
"""This python script defines a class Rectangle"""


class Rectangle:
    """
    A Class that defines the properties of the rectangle (based on 1-rectangle.py).

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """This Creates new instances of Rectangle.

        Args:
            width (int, optional): The width of rectangle. Defaults to 0.
            height (int, optional): The height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves the width.

        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """The property setter for width of rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """The Property setter for height of recyangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """This function Calculates area of a rectangle.

        Returns:
            int: area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """This function Calculates the perimeter of a rectangle

        Returns:
            int: the perimeter.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)
