was = {}


def count(x, y, n, left):
    if (x, y, left) in was:
        return was[(x, y, left)]
    if left == 0:
        return 1
    tot = 0
    for i in range(n - x - y + 1):
        tot += count(y, i, n, left - 1)
    was[(x, y, left)] = tot
    return tot


def total():
    tot = 0
    for i in range(1, 10):
        for j in range(10 - i):
            tot += count(i, j, 9, 18)
    return tot
