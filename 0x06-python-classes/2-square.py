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

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
