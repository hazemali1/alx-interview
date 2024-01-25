#!/usr/bin/python3
"""read stdin"""
import sys


if __name__ == '__main__':
    """main"""
    count = 0
    summ = 0
    li = {}

    try:
        for line in sys.stdin:
            s = line.split()
            if len(s) > 2:
                count += 1
                summ += int(s[-1])
                status = s[-2]
                if status in li.keys():
                    li[status] += 1
                elif status in ["200", "301", "400", "401", "403", "404", "405", "500"]:
                    li[status] = 1
                if count == 10:
                    count = 0
                    print("File size: {}".format(summ))
                    for k, v in sorted(li.items()):
                        print("{}: {}".format(k, v))

    finally:
        print("File size: {}".format(summ))
        for k, v in sorted(li.items()):
            print("{}: {}".format(k, v))
