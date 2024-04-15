#!/usr/bin/python3
"""function that check an object for a instance"""


def is_same_class(obj, a_class):
    """checks if a_class is an instance of obj

    Args:
        obj (any): an object
        a_class (any): instance of obj

    Returns:
        boolean: true or false
    """
    if type(obj) not in [a_class]:
        return False
    else:
        return True
