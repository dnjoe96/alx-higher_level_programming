#!/usr/bin/python3
def uppercase(sr):
    for s in sr:
        if ord(s) >= 97 and ord(s) <= 122:
            s_val = (ord(s) - 32)
        else:
            s_val = ord(s)
        print("{:c}".format(s_val), end="")
    print("")
