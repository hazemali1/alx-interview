#!/usr/bin/python3
"""UTF8"""


def validUTF8(data):
    i = 0
    while i < len(data):
        byte = data[i]
        if byte & 0b10000000 == 0:  # 1-byte character
            i += 1
        elif byte & 0b11100000 == 0b11000000:  # 2-byte character
            i += 2
        elif byte & 0b11110000 == 0b11100000:  # 3-byte character
            i += 3
        elif byte & 0b11111000 == 0b11110000:  # 4-byte character
            i += 4
        else:
            return False

        if i > len(data) or byte > 255:
            return False

    return True
