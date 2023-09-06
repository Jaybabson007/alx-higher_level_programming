#!/usr/bin/python3
"""This python script defines a class LockedClass"""


class LockedClass:
    """
    This class prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.

    Attributes:
        first_name (str): The first name.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """This functiion creates new instances of Locked Class."""

        self.first_name = "first_name"

