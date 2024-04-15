#!/usr/bin/python3
"""checkes for a subclass"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
    obj: Any Python object
    a_class: Class or type to compare against

    Returns:
    bool: True if the object is an instance of a subclass
    otherwise False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
