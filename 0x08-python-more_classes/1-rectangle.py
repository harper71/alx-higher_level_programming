#!/usr/bin/python3
"""a rectangle class
"""


class Rectangle:
    def __init__(self, width=0, height=0):

        """a rectangle that creates a rectangle

        Args:
            width (int): width of rectangle. Defaults to 0.
            height (int): height of rectangle. Defaults to 0.
        """
        self.__validate_size(height)
        self.__validate_size2(width)

        self.__height = height
        self.__width = width

    def __validate_size(self, height):
        """Validates the size of the rectangle.

        Raises:
            ValueError: height must be >= 0
            TypeError: height must be an integer
        """

        if type(height) not in [int]:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def __validate_size2(self, width):
        """Validates the size of the rectangle.

        Raises:
            ValueError: width must be >= 0
            TypeError: width must be an integer
        """

        if type(width) not in [int]:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
