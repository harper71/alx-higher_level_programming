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
