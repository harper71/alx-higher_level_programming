#!/usr/bin/python3
"""a rectangle class
"""


class Rectangle:
    """ a rectangle shape"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):

        """a rectangle that creates a rectangle

        Args:
            width (int): width of rectangle. Defaults to 0.
            height (int): height of rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """calculate the area of a rectangle

        Returns:
            int: width * height
        """

        return self.__width * self.__height

    def perimeter(self):
        """perimeter of rectangle

        Returns:
            int: 2(width + height)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ this function prints the "#" in the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += "#" * self.__width + "\n"
            return rectangle_str.rstrip("\n")

    def __repr__(self):
        Rectangle.number_of_instances += 1
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
