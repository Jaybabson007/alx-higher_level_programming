#!/usr/bin/python3
"""A module containing the function write_file"""


def write_file(filename="", text=""):
    """This function writes a string to a text file (UTF8) and returns the number
    of characters written.

    Args:
        filename (str, optional): The name of the file, it defaults to "".
        text (str, optional):The  string of text to write to file, it defaults to "".

    Returns:
        int: The number of characters written to file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        """This method returns the number of characters written to a file."""
        return f.write(text)
