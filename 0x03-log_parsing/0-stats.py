#!/usr/bin/python3
"""read stdin"""
import sys


count = 0
summ = 0 
l = {}


try:
    for line in sys.stdin:
        s = line.split()
        count += 1
        summ += int(s[-1])
        status = s[-2]
        if status in l.keys():
            l[status] += 1
        else:
            l[status] = 1
        if count == 10:
            count = 0
            print("File size: {}".format(summ))
            ll = {key: l[key] for key in sorted(l)}
            for k, v in ll.items():
                print("{}: {}".format(k, v))

except KeyboardInterrupt:
    print("File size: {}".format(summ))
    ll = {key: l[key] for key in sorted(l)}
    for k, v in ll.items():
        print("{}: {}".format(k, v))

