#!/usr/bin/python3
"""creates an empty class"""


class BaseGeometry:
    """class of geometries"""

    def area(self):
        """raises an error"""

    def integer_validator(self, name, value):
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""class that creates a rectangle subclass"""


class Rectangle(BaseGeometry):
    """a rectangle class

    Args:
        BaseGeometry (int): a rectangle
    """
    def __init__(self, width, height):
        super().__init__()

        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


""" a subclass of a rectangle class"""


class Square(Rectangle):
    """a square class

    Args:
        Rectangle (int): a square
    """
    def __init__(self, size):
        self.__size = size
        Rectangle.__init__(self, width=size, height=size)

        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size
