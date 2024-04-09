#!/usr/bin/python3
"""
this is a add module.
this adds two numbers either int or float

>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """" function to add two numbers
    Args:
        a (int, float): takes a number
        b (int, float): takes an number. Defaults to 98.
    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer
    Returns:
        int : a + b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
