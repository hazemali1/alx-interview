#!/usr/bin/python3
"""UTF8"""


def validUTF8(data):
    """valid UTF8"""
    j = 0
    s = 0
    while j < len(data):
        i = data[j]
        if format(i, '08b')[0] == '0':
            s += 1
        elif format(i, '08b')[0:3]== '110':
            s += 2
        elif format(i, '08b')[0:4] == '1110':
            s += 3
        elif format(i, '08b')[0:5] == '11110':
            s += 4
        else:
            return False

        j = s
        if j > len(data) or i > 255:
            return False
    return True
