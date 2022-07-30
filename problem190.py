from fractions import Fraction


def tri(n):
    return n * (n + 1) // 2


def p(x):
    res = 1
    for i in range(len(x) - 1):
        res *= x[i + 1] ** (i + 1)
    return int(res)


def gen_x(n):
    return [0] + [Fraction(n * i, tri(n)) for i in range(1, n + 1)]


def ans():
    return sum([p(gen_x(i)) for i in range(2, 16)])
