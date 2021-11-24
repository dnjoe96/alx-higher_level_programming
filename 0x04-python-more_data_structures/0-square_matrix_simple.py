#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = []
    for i in matrix:
        lis = []
        for j in i:
            lis.append(j * j)
        new_mat.append(lis)
    return new_mat
