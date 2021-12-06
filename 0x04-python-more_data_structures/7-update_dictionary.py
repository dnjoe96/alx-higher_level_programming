#!/usr/bin/python3
def weight_average(my_list=[]):
    _sum = 0
    count = 0
    for elem in my_list:
        prod = elem[0] * elem[1]
        _sum += prod
        count += 1
    return _sum / count
