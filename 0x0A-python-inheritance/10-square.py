#!/usr/bin/python3
"""module for Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size):
        """initialization of square"""
        super().integer_validator('size', size)
        self.__size = size

    def area(self):
        """Area"""
        return self.__size ** 2
