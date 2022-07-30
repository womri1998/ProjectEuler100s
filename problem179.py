import math


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(math.ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


def consecutive_divisors(n):
    primes = gen_primes(n)
    print("ok")
    divisors = [1] * n
    for p in primes:
        for i in range(1, n // p + 1):
            if i % p != 0:
                x = i * p
                j = 2
                while x < n:
                    divisors[x] *= j
                    j += 1
                    x *= p
    res = 0
    for i in range(2, len(divisors) - 1):
        if divisors[i] == divisors[i + 1]:
            res += 1
    return res
