#!/usr/bin/python3
"""Module for rotating a 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotate the matrix 90 degrees clockwise in-place"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
