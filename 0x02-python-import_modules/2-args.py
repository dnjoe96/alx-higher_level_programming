#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    if len(argv) < 2:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("{:d} argument:".format(len(argv) - 1))
        else:
            print("{:d} arguments:".format(len(argv) - 1))
    for arg in argv[1:]:
        print("{:d}: {:s}".format(i, arg))
        i += 1
