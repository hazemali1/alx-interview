#!/usr/bin/python3
"""N queens for chess"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

num = int(sys.argv[1])
lis = []
d = 1

for j in range(num - 2):
    li = []
    for i in range(num):
        if len(li) == 0:
            s = d
        elif len(li) == num - 1:
            s = 0
        elif len(li) == d - 1:
            s = 1
        else:
            s = i + 1
        li.append([i, s])
    lis.append(li)
    d += 1

for x in lis:
    print(x)
