#!/usr/bin/python3


class Square:
    """a square class
    """

    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.__position = position

    def __ValidateSize(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def __validatePosition(self, postion):

        if not isinstance(postion, tuple) or len(postion) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) and x >= 0 for x in postion):
            raise TypeError("position must be a tuple of 2 positive integers")

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

        self.__ValidateSize(value)
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):

        self.__validatePosition(value)
        self.__position = value

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
        if self.__position[1] > 0:
            print()
        
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
