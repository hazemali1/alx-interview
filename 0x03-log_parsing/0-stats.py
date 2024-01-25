#!/usr/bin/python3
"""read stdin"""
import sys


count = 0
summ = 0 
l = {}


try:
    for line in sys.stdin:
        s = line.split()
        print(s)
        count += 1
        summ += s[-1]
        status = s[-2]
        if status in l.keys():
            l[status] += 1
        else:
            l[status] = 1
        if count == 10:
            count = 0
            print("File size: {}".format(summ))
            for k, v in l.items():
                print("{}: {}".format(k, v))

except KeyboardInterrupt:
    print("File size: {}".format(summ))
