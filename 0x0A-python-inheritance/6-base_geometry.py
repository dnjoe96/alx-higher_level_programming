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
