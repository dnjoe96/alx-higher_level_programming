#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    _sum = 0
    count = 0
    for elem in my_list:
        prod = elem[0] * elem[1]
        _sum += prod
        count += elem[1]
    return _sum / count
