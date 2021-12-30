#!/usr/bin/python3
""" module for print_indentation function """


def text_indentation(text):
    """ texr_indentation function """
    if type(text) is not str:
        raise TypeError("text must be a string")
    y = "-"
    for x in text:
        if y not in [".", "?", ":"]:
            print(x, end="")
        y = x
        if x in [".", "?", ":"]:
            print("\n")
