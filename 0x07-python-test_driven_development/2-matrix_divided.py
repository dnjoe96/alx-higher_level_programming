#!/usr/bin/python3
""" The module contain matrix_divided function """


def matrix_divided(matrix, div):
    """Function to divide a matrix by a div"""
    nsize = 0
    psize = 0

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    mainlist = []
    for idx, row in enumerate(matrix):
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats")
        nsize = len(row)
        if nsize != psize and psize != 0:
            raise TypeError('Each row of the matrix must have the same size')
        else:
            psize = nsize

        sub = []
        for a in row:
            if type(a) not in [int, float]:
                raise TypeError('matrix must be a matrix (list of lists) \
                        of integers/floats')

            result = a / div
            if result == float('inf') or result == -float('inf'):
                return 89

            sub.append(round(result, 2))
        mainlist.append(sub)

    return mainlist
