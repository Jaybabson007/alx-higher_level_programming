#!/usr/bin/python3
"""A module defining the class Student based on the 10-student.py file"""


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

        If the argument attrs is a list of strings, only attribute names contained in
        this list must be retrieved. Else all attributes must be retrieved.

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

    def reload_from_json(self, json):
        """This function replaces all attributes of the Student instance.

        Args:
            json (dict): A json object.
        """

        # print("Type json --> {}".format(type(json)))
        self.__dict__.update(json)
