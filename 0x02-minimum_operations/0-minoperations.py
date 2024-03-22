#!/usr/bin/python3
"""
Find Minimum Operations
"""


def minOperations(n):
    """
    calculate the minimum operations
    """
    num = n
    div = 2
    op = 0

    while (num > 1):
        if num % div == 0:
            num = int(num / div)
            op += div
            div = 2
        else:
            div += 1

    return op
