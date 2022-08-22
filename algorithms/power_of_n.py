'''Use this to check if a number is a power of n'''

import math


def power_of_n(x: int, y: int) -> bool:
    # The only power of 1
    # is 1 itself
    if (x == 1):
        return (y == 1)

    # Repeatedly compute
    # power of x
    pow = 1
    while (pow < y):
        pow = pow * x

    # Check if power of x
    # becomes y
    return (pow == y)
