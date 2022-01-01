#!/usr/bin/python3
""" Module for the Rectangle class """
from .base import Base


class Rectangle(Base):
    """ The Rectangle class 
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be > 0')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be > 0')
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def display(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        y = self.__y
        for i in range(self.__height + y):
            if y == 0:
                x = self.__x
                for j in range(self.__width + x):
                    if x == 0:
                        print("#", end="")

                    else:
                        x -= 1
                        print(" ", end="")
                print("")

            else:
                y -= 1
                print("")
    
    def update(self, *args, **kwargs):
        i_d = args[0] if len(args) > 0 else self.id
        i_d = kwargs['id'] if 'id' in kwargs.keys() else i_d
        width = args[1] if len(args) > 1  else self.__width
        width = kwargs['width'] if 'width' in kwargs.keys() else width
        height = args[2] if len(args) > 2 else self.__height
        height = kwargs['height'] if 'height' in kwargs.keys() else height
        x = args[3] if len(args) > 3 else self.__x
        x = kwargs['x'] if 'x' in kwargs.keys() else x
        y = args[4] if len(args) > 4 else self.__y
        y = kwargs['y'] if 'y' in kwargs.keys() else y

        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be > 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be > 0')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"[Rectangle ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
