#!/usr/bin/python3
"""
Pascal's Triangle
"""
def pascal_triangle(n):
    """
    Returns list of int representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
