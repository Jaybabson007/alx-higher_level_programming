#!/usr/bin/python3
"""this is a module containing the function read_file"""


def read_file(filename=""):
    """This function reads a file and prints it to stdout.

    Args:
        filename (str, optional):The name of the file to read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
