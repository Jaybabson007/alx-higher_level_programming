#!/usr/bin/python3
# 4-print_square.py
"""The python file defines a square-printing function."""


def print_square(size):
    """This function prints a square with the pound # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")

