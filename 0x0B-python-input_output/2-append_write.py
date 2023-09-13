#!/usr/bin/python3
"""A module containing the function append_write"""


def append_write(filename="", text=""):
    """This function appends a string to a text file (UTF8) and returns the number
    of characters added.

    Args:
        filename (str, optional): The name of the file. Defaults to "".
        text (str, optional): The string of text to write to file. Defaults to "".

    Returns:
        int: Returns the number of characters appended to file.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        """This method returns the number of characters appended to a file."""
        return f.write(text)
