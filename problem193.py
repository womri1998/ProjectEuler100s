from math import ceil


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(ceil(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]
