#!/usr/bin/python3
""" Module for the Square class """
from .base import Base
from .rectangle import Rectangle


class Square(Rectangle):
    """ The Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor
        Args:
            id (int): The instance id.
            width (int): The size of each side of the square.
            x (int): Horizontal padding.
            y (int): Vertical padding.
        """
        self.__size = size
        super().__init__(size, size, x, y, id=id)

    @property
    def size(self):
        """Returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the value of size"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the properties of the class object
        Args:
            *args:
                args[0]: id (int): The instance id.
                args[1]: size (int): The length of the size of the square
                args[2]: x (int): Horizontal padding.
                args[3]: y (int): Vertical padding.
            **kwargs:
                id (int): The instance id.
                size (int): The length of the size of the Square
                x (int): Horizontal padding.
                y (int): Vertical padding.
        """
        i_d = args[0] if len(args) > 0 else self.id
        i_d = kwargs['id'] if 'id' in kwargs.keys() else i_d
        size = args[1] if len(args) > 1 else self.size
        size = kwargs['size'] if 'size' in kwargs.keys() else size
        x = args[2] if len(args) > 2 else self.x
        x = kwargs['x'] if 'x' in kwargs.keys() else x
        y = args[3] if len(args) > 3 else self.y
        y = kwargs['y'] if 'y' in kwargs.keys() else y

        self.id = i_d
        self.width = size
        self.height = size
        self.x = x
        self.y = y

    def to_dictionary(self):
        """Returns the dictionary of a class instance attribute"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """Returns the string representation of an instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
