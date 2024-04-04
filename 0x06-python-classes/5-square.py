#!/usr/bin/python3

"""This is a square module that creates a square class."""


class Square:
    """a square class
    """
    def __init__(self, size=0):
        """initalizes the size of the sqaure class

        Args:
            size (int, optional): size of square. Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__validate_size(size)
        self.__size = size

    def __validate_size(self, size):
        """Validates the size of the square.

        Raises:
            ValueError: If the size is less than or equal to 0.
            TypeError: If the size is not an integer.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.__validate_size(value)
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        result = self.__size * self.__size
        return result

    def my_print(self):
        """Prints a square using '#' characters based on the size.

            prints the square pattern.
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
