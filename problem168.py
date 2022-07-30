def good(l, n, m, d):
    x, y = (10 ** l - d) * m, 10 * d - 1
    k = x // y - n * 10 ** (l - 1)
    if x % y == 0 and 0 <= k < 10 ** (l - 1):
        z = n * 10 ** l + 10 * k + m
        return z % 10 ** 5
    else:
        return 0


def l_digits(l):
    res = 0
    for n in range(1, 10):
        for m in range(1, 10):
            for d in range(1, 10):
                res += good(l - 1, n, m, d)
    return res % 10 ** 5


def total():
    return sum([l_digits(i) for i in range(101)]) % 10 ** 5
