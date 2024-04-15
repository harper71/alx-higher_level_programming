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
