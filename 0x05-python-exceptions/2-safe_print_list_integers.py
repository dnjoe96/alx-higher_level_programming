#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for n in range(x):
        item = my_list[n]
        try:
            print("{:d}".format(item), end="")
            count += 1
        except Exception:
            continue
    print("")
    return count
