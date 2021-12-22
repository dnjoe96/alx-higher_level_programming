#!/usr/bin/python3
"""module for task 1"""


def read_file(filename=""):
    """read a file"""
    with open(filename) as f:
        print(f.read(), end="")
