#!/usr/bin/python3
"""Module for Minimum Operations problem"""


def minOperations(n):
    """Calculate the fewest number of operations to reach n H characters"""
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
