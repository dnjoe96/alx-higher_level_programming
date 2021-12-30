#!/usr/bin/python3
"""module for MyInt class"""


class MyInt(int):
    """Inverts the int operations != and =="""

    def __eq__(self, value):
        """invert and overwrite the == operation"""
        return self.real != value

    def __ne__(self, value):
        """invert and overrite the != operation"""
        return self.real == value
