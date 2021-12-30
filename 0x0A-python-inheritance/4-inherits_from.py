#!/usr/bin/python3
"""module for task four"""


def inherits_from(obj, a_class):
    """
    True if the object is an instance of a class that inherited
    either directly or indirectly from the specified class else False
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)
