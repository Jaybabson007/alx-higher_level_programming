#!/usr/bin/python3
"""A module defining the class Student based on the 9-student.py file"""


class Student:
    """
    A Class that defines properties of student.

    Attributes:
        first_name (str): The first name of student.
        last_name (int): The last name of student.
        age (int): The age of student.
    """
    def __init__(self, first_name, last_name, age):
        """This function creates new instances of Student.

        Args:
            first_name (str): The first name of student.
            last_name (int): The last name of student.
            age (int): The age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function retrieves a dictionary representation of a Student instance.

        If attr is a list of strings then only attribute names contained in
        this list must be retrieved.
        else, all attributes must be retrieved.

        Returns:
            dict: A dictionary representation.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict
