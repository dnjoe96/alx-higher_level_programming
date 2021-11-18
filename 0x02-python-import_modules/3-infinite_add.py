#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    isum = 0
    for n in argv[1:]:
        isum += int(n)
    print("{:d}".format(isum))
