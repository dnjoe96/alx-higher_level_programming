#!/usr/bin/python3
""" module for print_square function"""


def print_square(size):
    """ function to print square of size size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print("")
