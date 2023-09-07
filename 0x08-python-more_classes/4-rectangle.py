#!/usr/bin/python3
#4-rectangle.py
"""This python script defines a class Rectangle"""


class Rectangle:
    """
    A Class that defines the properties of a rectangle(based on 3-rectangle.py).

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """This function creates new instances of Rectangle.

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
            int: returns the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Retrieves the height.

        Returns:
            int: returns the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """This function acts as a property setter for width of rectangle.

        Args:
            value (int): The width of the rectangle.

        Raises:
            TypeError: if the width is not an integer.
            ValueError: if the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """This function acts as a property setter for height of rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: if the height is not an integer.
            ValueError: if the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """This function Calculates the area of a rectangle.

        Returns:
            int: returns the area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """This function calculates the perimeter of a rectangle

        Returns:
            int: returns the perimeter.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """This prints the rectangle with the character # .

        Returns:
            str: the rectangle
        """
        rectangle = []

        if self.__width == 0 or self.__height == 0:
            return ""

        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")

        # remove blank line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """This returns a string representation of the rectangle.

        Returns:
            str: the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
