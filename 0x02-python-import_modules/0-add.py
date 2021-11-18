#!/usr/bin/env python3
iadd = __import__('add_0').add
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(1, 2, iadd(1, 2)))
