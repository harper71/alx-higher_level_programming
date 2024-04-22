
from models.rectangle import Rectangle
"""This is a square module that creates a square class."""


class Square(Rectangle):
    """creates a sub_class of rectangle called square

    Args:
        Rectangle (class): rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.size}"
    
    @property
    def size(self):
        return self.__width
    
    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value
    def update(self, *args, **kwargs):
        """this uses the args and kwargs
            to take variable numbers of arguments
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.__x = args[2]
        if len(args) >= 4:
            self.__y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value
    def to_dictionary(self):
        """gets the dictionary of square

        Returns:
            dictionary: returns a dictionary of all square elements
        """
        return self.__dict__