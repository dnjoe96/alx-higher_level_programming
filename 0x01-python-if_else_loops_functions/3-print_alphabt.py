#!/usr/bin/python3
for x in range(1, 27):
    if x not in [5, 17]:
        print("{:c}".format(96 + x, end=""), end="")
