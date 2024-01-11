#!/usr/bin/python3
"""canUnlockAll"""


def canUnlockAll(boxes):
    """function to un lock all boxes if it can be unlocked"""
    boxess = boxes[:]
    lis = []
    if (len(boxess) == 1):
        return True
    for box in range(len(boxess)):
        if box not in lis and box != 0:
            continue
        for i in range(len(boxess[box])):
            if boxess[box][i] not in lis and boxess[box][i] != 0 and boxess[box][i] != box:
                if boxess[box][i] < box and boxess[box][i] not in lis:
                    for j in boxess[boxess[box][i]]:
                        if j not in lis and j != 0:
                            lis.append(j)
                lis.append(boxess[box][i])
    for k in range(len(boxess)):
        if k != 0 and k not in lis:
            return False
    return True
