#!/usr/bin/python3

"""This is a square module that creates a square class."""


class Square:
    """A class representing a Square.

        This class represents a square and provides methods
        such as initializing the square with a given size.

        Attributes:
            __size (any): The size of the square.
    """

    def __init__(self, size):
        """Initializes the square with a given size.

        Args:
            size (any): The size of the square.
        """
        self.__size = size
