"""
Stanford Assignment 1: Multiply two numbers using Karatsuba algorithm
https://en.wikipedia.org/wiki/Karatsuba_algorithm

"""


def split_at(n, m):
    """
    :param n: numbers
    :param m: split index
    :return: tuple of ints split at m
    """
    n = str(n)
    n1 = int(n[:m])
    n2 = int(n[m:])
    return n1, n2


def num_len(n):
    """
    :param n: numbers
    :return: amount of digits
    """
    return len(str(abs(n)))


def karatsuba(n1, n2):
    """
    :param n1: 1st number
    :param n2: 2nd number
    :return: product of 1st number and 2nd number

    ex:
    num1 = 5678
    num2 = 1234

    high1 = 56
    low1 = 78
    high2 = 12
    low2 = 34

    Recursively compute
    (1) low1 * low2
    (2) (low1 + high1) * (low2 + high2)
    (3) high1 * high2

    return Gauss equation and pad numbers
    2 + (2 - 3 - 1) + 1

    """
    # base case of single digit
    if n1 < 10 or n2 < 10:
        return n1 * n2

    # split number
    m = max(num_len(n1), num_len(n2))
    m2 = m / 2
    high1, low1 = split_at(n1, m2)
    high2, low2 = split_at(n2, m2)

    # recursively compute
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    #
    return (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0
