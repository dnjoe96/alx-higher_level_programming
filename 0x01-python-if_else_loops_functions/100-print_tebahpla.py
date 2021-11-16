#!/usr/bin/python3
n = 25
for x in range(26):
    val = n - x
    if x % 2 == 0:
        val = 97 + n - x
    else:
        val = 65 + n - x
    print("{:c}".format(val), end="")
