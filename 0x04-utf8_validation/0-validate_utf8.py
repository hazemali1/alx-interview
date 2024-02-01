#!/usr/bin/python3
"""UTF8"""


def validUTF8(data):
    """valid UTF8"""
    for i in data:
        if i > 255:
            return False
    return True
