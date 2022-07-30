def count_undivisibles(n):
    res = 1
    while n != 0:
        res *= n % 7 + 1
        n //= 7
    return res


def total_undivisibles2(n):
    tot = 0
    for i in range(n):
        tot += count_undivisibles(i)
    return tot


def max_7(n):
    if n == 0:
        return 0
    i = 0
    while 7 ** i <= n:
        i += 1
    return i


def total_undivisibles(n):
    res = 0
    i = 0
    while n != 0:
        res *= n % 7 + 1
        res += 28 ** i * sum([i for i in range(n % 7 + 1)])
        i += 1
        n //= 7
    return res
