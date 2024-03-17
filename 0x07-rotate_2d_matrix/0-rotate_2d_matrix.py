#!/usr/bin/python3
"""2D matrix to rotate"""


def rotate_2d_matrix(matrix):
    """rotates the matrix 90 degrees"""
    rev = matrix[::-1]
    li = []
    for o in range(len(rev)):
        for t in range(len(rev[o])):
            if o == 0:
                j = []
                j.append(rev[o][t])
                li.append(j)
            else:
                li[t].append(rev[o][t])
    for f in range(len(matrix)):
        matrix.pop()
    for h in range(len(li)):
        matrix.append(li[h])
