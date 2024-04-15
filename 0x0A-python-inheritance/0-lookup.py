#!/usr/bin/python3
"""looks up all method and object in a class"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
    obj: Any Python object

    Returns:
    List: List of available attributes and methods of the object
    """

    return dir(obj)
