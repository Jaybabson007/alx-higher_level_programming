#!/usr/bin/python3

import math


class MagicClass:
    """This class represent the 
    blueprint of a circle."""

    def __init__(self, radius=0):
        """This function initializes a MagicClass.

        Argument:
        radius (float or int): radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """This function returns the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """This function returns The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
