def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(n):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


primes = gen_primes(10 ** 6)


def iter_squaring(x, y, n):
    res = 1
    i = 1
    j = x % n
    while i <= y:
        if y & i != 0:
            res *= j
        i *= 2
        j = mod_mul(j, j, n)
    return res


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


def remainder(n):
    return (iter_squaring(primes[n - 1] - 1, n, primes[n - 1] ** 2) + iter_squaring(primes[n - 1] + 1, n, primes[n - 1] ** 2)) % primes[n - 1] ** 2


