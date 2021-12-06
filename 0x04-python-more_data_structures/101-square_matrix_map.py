#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda x: x * x, matrix[0])), list(map(lambda x: x * x, matrix[1]))]
