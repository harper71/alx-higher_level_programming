#!/usr/bin/python3

"""Represents a square with size and position."""


class Square:
    """a square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with optional size and position."""
        self.__size = size
        self.__position = position

    def __ValidateSize(self, size):
        """Validates the size of the square.

        Raises:
            ValueError: If the size is less than or equal to 0.
            TypeError: If the size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def __validatePosition(self, postion):
        """validates position to an int

        Args:
            postion (int): returns a integer

        Raises:
            TypeError: position must be a tuple of 2 positive integers
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(postion, tuple) or len(postion) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in postion):
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.__ValidateSize(value)
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for square

        Args:
            value (int): postion of the square
        """
        self.__validatePosition(value)
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        result = self.__size * self.__size
        return result

    def my_print(self):
        """Prints a square using '#' characters based on the size.
            and positions 
            prints the square pattern.
        """

        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            print()
        
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
