#!/usr/bin/python3
"""This script defines a class called MyInt that inherits int.
MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """ MyInt class.

    Args:
        int (int): the value
    """
    def __init__(self, value):
        """This function creates new instances of class MyInt.

        Args:
            value (int): The integer.
        """
        self.__value = value

    def __eq__(self, other):
        """This function defines the method equal

        Args:
            other (int): An integer.

        Returns:
            boolean: returns True or False.
        """
        return self.__value != other

    def __ne__(self, other):
        """This function defines the method not equal

        Args:
            other (int): An integer.

        Returns:
            boolean: Returns True or False
        """
        return self.__value == other
