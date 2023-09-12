#!/usr/bin/python3
"""The python script defines a function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """This function returns True if the object is an instance of or if the object is,
    an instance of a class that inherited from, the specified class,
    else it returns False

    Args:
        obj (a_class): The object to check type.
        a_class (type): type of type to check.

    Returns:
        A boolean: True or False.
    """

    return isinstance(obj, a_class)
