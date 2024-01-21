#!/usr/bin/python3
"""min operations"""
def minOperations(n):
    """min operations"""
    if n <= 1:
        return 0
    f = 0
    l = 0
    for i in range(2, n):
        if n % i == 0:
            if f == 0 or (f - l > 0 and i - n / i >= 0 and f - l > i - n / i):
                l = i
                f = n / i
    return int(f + l)
