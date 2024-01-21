#!/usr/bin/python3
"""min operations"""


def minOperations(n):
    """min operations"""
    if n <= 1:
        return 0
    f = 2
    l = 0
    while f <= n:
        if n % f == 0:
            print(f)
            l += f
            n = n / f
        else:
            f += 1
    return l
