#!/usr/bin/python3
"""
This module defines a class where attributes cannot be created 
from objects unless it is a certain name
"""


class LockedClass:
    """
    class that allows only one attribute creation
    """
    __slot__ = 'first_name'

    def __init__(self, name=''):
        """
        Initializes new objects
        """
        self.first_name = name
