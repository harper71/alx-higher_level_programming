#!/usr/bin/python3
"""set an attribute to a new object"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception if the object can't have new attributes.

    Args:
    obj: Any Python object
    attr_name: Name of the attribute to be added
    attr_value: Value of the attribute to be added
    """

    if hasattr(obj, '__dict__') or hasattr(obj, '__slots__') \
            or hasattr(type(obj), '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
