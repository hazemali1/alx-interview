#!/usr/bin/python3
"""UTF8"""


def validUTF8(data):
    """valid UTF8"""
    j = 0
    while j < len(data):
        i = data[j]
        if format(i, '08b')[0] == '0':
            j += 1
        elif format(i, '08b')[0:3]== '110':
            j += 2
        elif format(i, '08b')[0:4] == '1110':
            j += 3
        elif format(i, '08b')[0:5] == '11110':
            j += 4
        else:
            return False
        if j > len(data) or i > 255:
            return False
    return True
