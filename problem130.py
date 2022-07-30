import math


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


def gen_composites(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(math.ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if i % 2 != 0 and i % 5 != 0 and (not primes[i])]


def property(n):
    cur, tot = 1, 1
    i = 1
    while tot != 0:
        cur = mod_mul(cur, 10, n)
        tot += cur
        tot %= n
        i += 1
    return (n - 1) % i == 0


def first_property(n):
    count, i, tot = 0, 1, 0
    comp = gen_composites(10 ** 6)
    while count != n:
        if property(comp[i]):
            print(i, comp[i], count, tot)
            count += 1
            tot += comp[i]
        i += 1
    return tot
