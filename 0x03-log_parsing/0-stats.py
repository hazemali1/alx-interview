#!/usr/bin/python3
"""read stdin"""
import sys


try:
    for line in sys.stdin:
        s = line.split()
        print(s)

except EOFError:
    print("End of input.")
