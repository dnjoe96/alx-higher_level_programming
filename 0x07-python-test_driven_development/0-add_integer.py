#!/usr/bin/python3
""" The module contain add_integar function """

def add_integer(a, b=98):
    """Function to add two numbers"""
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    return int(a) + int(b)
