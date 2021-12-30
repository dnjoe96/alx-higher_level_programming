#!/usr/bin/python3
"""module for task three"""


def is_kind_of_class(obj, a_class):
    """
    check is obj is instace of a_class
    even if obj isinstace of class that inherits from a_class
    """
    return isinstance(obj, a_class)
