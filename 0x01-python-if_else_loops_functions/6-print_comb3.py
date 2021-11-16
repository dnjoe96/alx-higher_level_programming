#!/usr/bin/python3
for x in range(10):
    for y in range(x, 10):
        if x == 0 and y == 1:
            print("{:d}{:d}".format(x, y), end="")
        elif not (x == 0 and y == 0) and x - y != 0:
            print(", {:d}{:d}".format(x, y), end="")
print("")
