#!/usr/bin/python3
"""appends if a string is seen"""


def append_after(filename="", search_string="", new_string=""):
    """functions appends new_string"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
