#!/usr/bin/python3
"""appends to file"""


def append_write(filename="", text=""):
    """appends text to afile

    Args:
        filename (str, optional): file name. Defaults to "".
        text (str, optional): text to append. Defaults to "".

    Returns:
        int: number of apended characters
    """
    with open(filename, 'a', encoding="utf-8") as file:
        append_file = file.write(text)
        return append_file
