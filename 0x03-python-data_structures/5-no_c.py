#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new_str = ""
    for i in my_string:
        if i in ["C", "c"]:
            continue
        new_str = new_str + i
    return new_str
