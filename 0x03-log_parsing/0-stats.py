#!/usr/bin/python3
"""read stdin"""


try:
    while True:
        line = input()
        print(line)

except EOFError:
    print("End of input.")
