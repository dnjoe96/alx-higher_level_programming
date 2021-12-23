#!/usr/bin/python3
"""module for task 12"""


def pascal_triangle(n):
    """generate the pascal trinagle"""
    mainlist = []

    for i in range(1, n + 1):
        sublist = []
        if i == 1:
            mainlist.append([1])
        elif i == 2:
            mainlist.append([1, 1])
        else:
            sublist.append(1)
            for j in range(len(mainlist[-1]) - 1):
                sublist.append(mainlist[-1][j] + mainlist[-1][j + 1])
            sublist.append(1)
            mainlist.append(sublist)
    return mainlist
