#!/usr/bin/python3
"""
Rotate a 2D matrix 90 degrees clockwise in-place.
"""

def rotate_2d_matrix(matrix):
    """
    Rotates the given 2D matrix 90 degrees clockwise in-place.

    :param matrix: A 2D list of integers.
    """
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    
    # Reverse each row
    for row in matrix:
        row.reverse()

