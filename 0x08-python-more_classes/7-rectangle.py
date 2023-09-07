#!/usr/bin/python3
#7-rectangle.py
"""The python script defines a class Rectangle"""


class Rectangle:
    """
    A Class that defines the properties of rectangle(based on 6-rectangle.py).

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This function creates new instances of Rectangle.

        Args:
            width (int, optional): The width of rectangle. Defaults to 0.
            height (int, optional): The height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width.

        Returns:
            int: returns the width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """retrieves the height.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """The Property setter for width of rectangle.

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
        """The Property setter for height of the rectangle.

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
        """This function calculates the area of a rectangle.

        Returns:
            int: area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """This function calculates the perimeter of a rectangle

        Returns:
            int: perimeter.
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
                rectangle.append(str(self.print_symbol))
            rectangle.append("\n")

        # This removes a blank line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """This Returns a string representation of the rectangle.

        Returns:
            str: the rectangle representation.
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        This Deletes an instance of a class
        """
        print("{:s}".format("Bye rectangle..."))
        type(self).number_of_instances -= 1
