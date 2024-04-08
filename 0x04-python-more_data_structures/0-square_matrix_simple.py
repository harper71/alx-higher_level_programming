#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    powers = [[pow(element, 2) for element in row] for row in matrix]
    return powers

matrix = [[1, 2, 3], [6, 7, 8]]
print("{}".format(square_matrix_simple(matrix)))