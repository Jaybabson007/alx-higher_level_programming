#!/usr/bin/python3
#1-rectangle.py
"""This python script defines a class Rectangle"""


class Rectangle:
    """
    A Class that defines the properties of rectangle by: (based on 0-rectangle.py).

    Attributes:
        width (int): the width of the rectangle.
        height (int): the height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """This Creates new instances of Rectangle.

        Args:
            width (int, optional): the width of rectangle. Defaults to 0.
            height (int, optional): the height of rectangle. Defaults to 0.
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
        """The Property setter for width of rectangle.

        Args:
            value (int): the width of the rectangle.

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
            value (int): height of the rectangle.

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
