#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []
    arr = []
    for s in range(n):
        if s > 0:
            copy_arr = small_arr
        small_arr = []
        for d in range(s + 1):
            if d == 0:
                small_arr.append(1)
            elif s == 1:
                small_arr.append(1)
            elif d < s:
                num = copy_arr[d - 1] + copy_arr[d]
                small_arr.append(num)
            else:
                small_arr.append(1)
        arr.append(small_arr)
    return arr
