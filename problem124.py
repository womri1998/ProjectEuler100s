def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(n):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


primes = gen_primes(10 ** 5)


def radical(n):
    r = 1
    for p in primes:
        if n == 1:
            return r
        if n % p == 0:
            n /= p
            r *= p
        while n % p == 0:
            n /= p
    return r


rad = [(radical(i), i) for i in range(1, 10 ** 5 + 1)]
rad.sort(key = lambda l: (l[0], l[1]))
