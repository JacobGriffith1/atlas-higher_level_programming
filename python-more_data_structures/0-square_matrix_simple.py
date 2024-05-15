#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMat = matrix.copy()

    for i in range(len(matrix)):
        newMat[i] = list(map(lambda x: x**2, matrix[i]))

    return (newMat)
