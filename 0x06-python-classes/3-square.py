#!/usr/bin/python3

"""This is a square module that creates a square class."""


class Square:
    """a square class"""
    def __init__(self, size=0):
        """initalizes the size of the sqaure class

        Args:
            size (int, optional): size of square. Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates and returns the area of the square."""
        result = self.__size * self.__size
        return result
