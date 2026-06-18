#!/usr/bin/python3
"""Module for Lockboxes problem"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened"""
    n = len(boxes)
    unlocked = {0}
    keys = [0]

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if key < n and key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n
