#!/usr/bin/python3
"""module for task 1"""


def write_file(filename="", text="", encode='utf-8'):
    """read a file"""
    with open(filename, "w") as f:
        nb = f.write(text)

    return nb
