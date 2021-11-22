#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    idx = len(my_list) - 1
    for i in my_list:
        print("{:d}".format(my_list[idx]))
        idx = idx - 1
