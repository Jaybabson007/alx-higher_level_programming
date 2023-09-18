#!/usr/bin/python3
"""This python script defines a class Rectangle
that inherits from Base"""

from models.base import Base

class Rectangle(Base):
    """
    This class that defines the properties of the Rectangle.

     Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): x.
        y (int): y.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """This function creates new instances of the rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): The identity number of rectangle it defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """This function prints the rectangle"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    @property
    def width(self):
        """
        This function retrieves the width of the rectangle

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """This function defines the property setter for width of the rectangle.

        Args:
            value (int): The width of rectangle.

        Raises:
            TypeError: if the width is not an integer.
            ValueError: if the width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        This function retrieves the height of the rectangle

        Returns:
            int: The height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This function defines the Property setter for height of rectangle.

        Args:
            value (int): The height of the rectangle.

        Raises:
            TypeError: if the height is not an integer.
            ValueError: if the height is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        this function retrives the value of x.

        Returns:
            int: x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This function defines the property setter for x.

        Args:
            value (int): x.

        Raises:
            TypeError: if x is not an integer.
            ValueError: if x is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        This function retrieves the value of y

        Returns:
            int: y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        this function defines the property setter for y.

        Args:
            value (int): y.

        Raises:
            TypeError: if y is not an integer.
            ValueError: if y is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This function calculates area of a rectangle.

        Returns:
            int: area.
        """
        return self.__width * self.__height

    def display(self):
        """
        This function prints in stdout the Rectangle
        instance with the character #."""
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        This function assigns an argument to each attribute

        Args:
            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
        """

        # print("args {}".format(type(args)))
        # print("kwargs {}".format(type(kwargs)))
        if args is not None and len(args) is not 0:
            list_atrr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atrr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This function returns the dictionary representation of a Rectangle.

        Returns:
            dict: rectangle.
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
