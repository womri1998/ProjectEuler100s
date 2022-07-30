from itertools import combinations
from math import ceil


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


primes = gen_primes(10 ** 6)


def primality_check(n):  # assuming list of primes named "primes" exists
    for p in primes:
        if p ** 2 >= n:
            return True
        if n % p == 0:
            return False


def check(a):
    n = 0
    for x in range(len(a)):
        n += a[x] * 10 ** x
    if len(str(n)) == len(a):
        return primality_check(n), n
    return False, 0


def m(l, d):
    i = 1
    while i <= l:
        for x in combinations([j for j in range(l)], i):
            for y in range(10 ** i):
                to_put = [(y // (10 ** k)) % 10 for k in range(i)]
                cur = [d] * l
                for k in range(i):
                    cur[x[k]] = to_put[k]
                if check(cur)[0]:
                    return i
        i += 1


def s(l, d):
    dif = m(l, d)
    total = 0
    for x in combinations([j for j in range(l)], dif):
        for y in range(10 ** dif):
            to_put = [(y // (10 ** k)) % 10 for k in range(dif)]
            cur = [d] * l
            for k in range(dif):
                cur[x[k]] = to_put[k]
            c = check(cur)
            if c[0]:
                total += c[1]
    return total
