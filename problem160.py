import math

def remove0(n):
    while n % 10 == 0:
        n //= 10
    return n


def mod_fact(m, n):
    res, twos, fives = 1, 0, 0
    for i in range(1, m + 1):
        j = i
        while j % 2 == 0:
            j //= 2
            twos += 1
        while j % 5 == 0:
            j //= 5
            fives += 1
        res = remove0(res * j) % n
    return res, twos, fives


def mod_mul(x, y, n):
    res = 0
    i = 1
    j = x % n
    while i <= y:
        if y & i != 0:
            res += j
            res %= n
        i *= 2
        j *= 2
        j %= n
    return res


def ord(x, n):
    res = 2
    x %= n
    y = mod_mul(x, x, n)
    while y != x:
        y = mod_mul(y, x, n)
        res += 1
        print(y, res)
    return res


def iter_squaring(x, y, n):
    res = 1
    i = 1
    j = x % n
    while i <= y:
        if y & i != 0:
            res *= j
            res %= n
        i *= 2
        j = mod_mul(j, j, n)
    return res


def count_twos(n):
    tot = 0
    while n != 0:
        n //= 2
        tot += n
    return tot


def count_fives(n):
    tot = 0
    while n != 0:
        n //= 5
        tot += n
    return tot

15625
2528
