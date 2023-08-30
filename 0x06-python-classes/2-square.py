#!/usr/bin/python3
"""This defines a class square"""

class Square:
    """This represents the blueprint of a square"""
    def __init__(self, size=0):
    """This initializes a new square

    Args:
        size(int): size of the new square
    """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
