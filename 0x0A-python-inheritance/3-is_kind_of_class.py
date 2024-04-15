#!/usr/bin/python3
"""function that checks an instance"""


def is_kind_of_class(obj, a_class):
    """checks of an istance of obj"""

    if isinstance(obj, a_class):
        return True
    else:
        return False
