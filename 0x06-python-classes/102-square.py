#!/usr/bin/python3


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """
        The function initializes a new square.

        """
        self.size = size

    @property
    def size(self):
        """This function is used to
        get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
      """This function return the current area of the square."""
        return (self.__size * self.__size)

    def __equalto__(self, other):
        """This function defines the == comparision to a Square."""
        return self.area() == other.area()

    def __notequalto__(self, other):
        """This function defines the != comparison to a Square."""
        return self.area() != other.area()

    def __lessthan__(self, other):
        """This function defines the < comparison to a Square."""
        return self.area() < other.area()

    def __lessthanequalto__(self, other):
        """This function defines the <= comparison to a Square."""
        return self.area() <= other.area()

    def __greaterthan__(self, other):
        """This fuction defines the > comparison to a Square."""
        return self.area() > other.area()

    def __greaterthanequalto__(self, other):
        """This fucntion defines the >= comparison to a Square."""
        return self.area() >= other.area()
