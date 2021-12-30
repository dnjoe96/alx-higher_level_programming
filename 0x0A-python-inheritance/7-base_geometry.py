#!/usr/bin/python3
"""module for BaseGeometry class"""


class BaseGeometry:
    """ Base Geometry class"""
    def __init__(self):
        """empty"""
        pass

    def area(self):
        """area function"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Integar validation function"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
