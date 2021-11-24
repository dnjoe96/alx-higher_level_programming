#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return

    for k, val in list(a_dictionary.items()):
        if val == value:
            a_dictionary.pop(k)
    return a_dictionary
