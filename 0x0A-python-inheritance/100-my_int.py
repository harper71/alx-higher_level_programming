#!/usr/bin/python3
"""converts to integer"""


class MyInt(int):
    """
    A subclass of int with inverted == and != operators.

    """
    def __eq__(self, other):
        """
        Override the == operator to return the result of !=
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to return the result of ==
        """
        return super().__eq__(other)
