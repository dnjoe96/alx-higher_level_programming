#!/usr/bin/python3
"""module for Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""
    def __init__(self, width, height):
        """Initialization of the object"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Area """
        return self.__height * self.__width

    def __str__(self):
        """Str"""
        return f"[Rectangle] {self.__width}/{self.__height}"
