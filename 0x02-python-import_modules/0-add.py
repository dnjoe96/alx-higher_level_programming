#!/usr/bin/env python3
iadd = __import__('add_0').add
if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, iadd(a, b)))
