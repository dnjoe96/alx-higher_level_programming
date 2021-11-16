#!/usr/bin/python3
def remove_char_at(sr, n):
    new_str = ""
    j = 0
    for i in range(len(sr)):
        if i != n:
            j += 1
        else:
            continue
        new_str += sr[i]

    return new_str
