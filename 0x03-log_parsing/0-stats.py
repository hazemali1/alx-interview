#!/usr/bin/python3
"""read stdin"""
import sys


count = 0


try:
    for line in sys.stdin:
        s = line.split()
        print(s)
        count += 1
        if count == 10:
            count = 0
            print("File size: <total size>")

except KeyboardInterrupt:
    print("File size: <total size>")
