#!/usr/bin/python3
"""module for task 2"""


def append_write(filename="", text="", encode='utf-8'):
    """read a file"""
    with open(filename, "a") as f:
        nb = f.write(text)

    return nb
