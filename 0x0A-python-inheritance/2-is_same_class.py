#!/usr/bin/python3
"""The python script defines a function is_same_class()"""


def is_same_class(obj, a_class):
    """This function returns True if the object is exactly an instance of the,
    specified class, else it returns  False

    Args:
        obj (a_class): The object to check type.
        a_class (type): type of type to check.

    Returns:
        A boolean- True or False
    """
    return type(obj) == a_class
