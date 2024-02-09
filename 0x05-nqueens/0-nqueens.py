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
t = []
d = 1

for j in range(int((num - 2) / 2)):
    li = []
    q = d
    for i in range(num):
        if len(li) == 0:
            s = d
        elif q < num:
            s = q
        elif q > num:
            q = 0
            s = 0
        li.append([i, s])
        q += 2
    lis.append(li)
    d += 1

t = lis[:]
lis.reverse()
for j in range(len(lis)):
    g = []
    for i in range(num):
        g.append([i, lis[j][(i + 1) * -1][1]])
    t.append(g)

for x in t:
    print(x)
