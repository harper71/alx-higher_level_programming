#!/usr/bin/python3
"""opens a file"""


def read_file(filename=""):
    """opens a file

    Args:
        filename (str): name of the file. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as file:
        f_contents = file.read()
        print(f_contents)
