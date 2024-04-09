#!/usr/bin/python3
"""changes the first and last names"""


def say_my_name(first_name, last_name=""):
    """prints the  fisrt and last names

    Args:
        first_name (str): first name
        last_name (str): last names. Defaults to "".

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
