#!/usr/bin/python3
"""This python script defines a class Square"""


from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Class that defines the properties of a square.

     Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): Value x.
        y (int): Value y.
        id (int): The identity of square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """This function creates new instances of Square

        Args:
            size (int): The width and height of the square.
            x (int, optional): x. Defaults to 0.
            y (int, optional): y. Defaults to 0.
            id (int, optional): The identity number of the square.
                                It Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        This function Prints a square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """This function defines the property retriever for size.

        Returns:
            int: The size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """This function defines the property setter for width of square.
        Args:
            value (int): The width of the square.
        Raises:
            TypeError: if the width is not an integer.
            ValueError: if the width is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """This function assigns an argument to each attribute

        Args:
            *args (tuple): arguments.
            **kwargs (dict): A double pointer to a dictionary.
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        This function returns the dictionary representation of a Square.

        Returns:
            dict: square.
        """
        dict1 = self.__dict__
        dict2 = {}
        dict2['id'] = dict1['id']
        dict2['size'] = dict1['_Rectangle__width']
        dict2['x'] = dict1['_Rectangle__x']
        dict2['y'] = dict1['_Rectangle__y']

        return dict2
