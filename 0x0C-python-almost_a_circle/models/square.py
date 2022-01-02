#!/usr/bin/python3
""" Module for the Square class """
from .base import Base
from .rectangle import Rectangle


class Square(Rectangle):
    """ The Rectangle class 
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        super().__init__(size, size, x, y, id=id)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        i_d = args[0] if len(args) > 0 else self.id
        i_d = kwargs['id'] if 'id' in kwargs.keys() else i_d
        size = args[1] if len(args) > 1  else self.size
        size = kwargs['size'] if 'size' in kwargs.keys() else size
        x = args[2] if len(args) > 2 else self.x
        x = kwargs['x'] if 'x' in kwargs.keys() else x
        y = args[3] if len(args) > 3 else self.y
        y = kwargs['y'] if 'y' in kwargs.keys() else y

        self.width = size
        self.height = size
        self.x = x
        self.y = y

    def to_dictionary(self):
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
