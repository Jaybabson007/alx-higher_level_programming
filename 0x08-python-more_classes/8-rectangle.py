#!/usr/bin/python3
#8-rectangle.py
"""This python script defines a class called Rectangle"""


class Rectangle:
    """
    A class that defines the properties of the rectangle by(based on 7-rectangle.py).

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This function creates new instances of Rectangle.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
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
        """Retrieves the height.

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
        """The Property setter for height of recyangle.

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
        """This function calculates area of a rectangle.

        Returns:
            int: area.
        """
        return self.__height * self.__width

    def perimeter(self):
        """This function calculates perimeter of a rectangle

        Returns:
            int: perimeter.
        """
        if self.__height == 0 or self.width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """This Prints the rectangle with the character # .

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
        """This returns a string representation of the rectangle.

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """This function computes the area of two rectangles and compares them.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: the rectangle with the biggest area, otherwise rect_1 if
            areas are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        return rect_2
