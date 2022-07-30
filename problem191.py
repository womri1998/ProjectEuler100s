absent = {}


def absent_only(n, x):
    if x == 3:
        return 0
    if n == 0:
        return 1
    if (n, x) in absent:
        return absent[(n, x)]
    else:
        y = absent_only(n - 1, x + 1) + absent_only(n - 1, 0)
        absent[(n, x)] = y
        return y


def late(n):
    return sum([absent_only(i, 0) * absent_only(n - i - 1, 0) for i in range(n)]) + absent_only(n, 0)
