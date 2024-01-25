#!/usr/bin/python3
"""read stdin"""
import sys


try:
    for line in sys.stdin:
        print(len(line), "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")

except EOFError:
    print("End of input.")
