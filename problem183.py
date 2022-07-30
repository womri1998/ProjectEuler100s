from fractions import Fraction
from math import log, e


def best(n):
    m = int(n // e)
    return m if m * log(n / m) > (m + 1) * log(n / (m + 1)) else m + 1


def terminating(n):
    m = Fraction(n, best(n)).denominator
    while m % 2 == 0:
        m //= 2
    while m % 5 == 0:
        m //= 5
    return m == 1


def d(n):
    return n if not terminating(n) else -1 * n


def res():
    return sum([d(i) for i in range(5, 10001)])
