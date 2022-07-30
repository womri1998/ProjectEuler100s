import math


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(math.ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


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


def first_divisible(n):
    cur, tot = 1, 1
    i = 1
    while tot != 0:
        cur = mod_mul(cur, 10, n)
        tot += cur
        tot %= n
        i += 1
    return i


def first_repunit_factors(n, m):
    count, tot, i = 0, 0, 3
    primes = gen_primes(10 ** 6)
    while count != m:
        if n % first_divisible(primes[i]) == 0:
            count += 1
            tot += primes[i]
            print(count, tot, i)
        i += 1
        if i % 100 == 0:
            print(i)
    return tot
