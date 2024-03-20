#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    powers = [[pow(element, 2) for element in row] for row in matrix]
    return powers
