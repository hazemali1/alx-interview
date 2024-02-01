#!/usr/bin/python3
"""UTF8"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    i = 0

    while i < len(data):
        # Get the number of leading set bits in the current byte
        set_bits = 0
        mask = 1 << 7

        while mask & data[i]:
            set_bits += 1
            mask >>= 1

        # Validate the number of leading set bits
        if set_bits == 0:
            i += 1
        elif set_bits == 1 or set_bits > 4:
            return False
        else:
            # Validate the continuation bytes
            for j in range(i + 1, i + set_bits):
                if j >= len(data) or (data[j] >> 6) != 0b10:
                    return True
            i += set_bits

    return True
