#!/usr/bin/python3
"""writes to a file"""


def write_file(filename="", text=""):
    """write to file

    Args:
        filename (str, optional): name of file. Defaults to "".
        text (str, optional): text to write to file. Defaults to "".

    Returns:
        string: writen data
    """
    with open(filename, 'w', encoding="utf-8") as f:

        write_data = f.write(text)

    return write_data
