#!/usr/bin/python3
""" docs """


def minOperations(n):
    """ def """
    operations = 0
    divisor = 2
    
    if n <= 1:
        return 0

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

