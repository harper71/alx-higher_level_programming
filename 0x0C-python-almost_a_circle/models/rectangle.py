#!/usr/bin/python3
from models.base import Base
"""creates a class of a rectangle"""



class Rectangle(Base):
    """class of a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def  height(self):
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

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) not in [int]:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, value):
        if type(value) not in [int]:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__x = value

    def area(self):
        """calculate the area of a rectangle

        Returns:
            int: width * height
        """
        return self.__width * self.__height

    def display(self):
        """diisplays "#" as a rectangle
        """
        if self.__x and self.__y:
            for _ in range(self.__y):
                print()
            for _ in range(self.__height):
                print(" " * self.__x + "#" * self.__width)
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        return f"[Rectange] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """this uses the args and kwargs
            to take variable numbers of arguments
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """gets the dictionary of rectangle

        Returns:
            dictionary: returns a dictionary of all rectangle elements
        """
        return self.__dict__