#!/usr/bin/python3
""" Module for the Square class """
from .base import Base
from .rectangle import Rectangle


class Square(Rectangle):
    """ The Rectangle class 
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        Rectangle.__init__(self, size, size, x, y, id=id)
    
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value

    @property
    def size(self, val):
        return self.__width

    def __str__(self):
        return "temporaty"
        # return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"
