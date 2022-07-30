def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(int(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


def euclidean(m, n):
    x, y = (max(m, n), 1, 0), (min(m, n), 0, 1)
    while y[0] != 0:
        x, y = y, (x[0] % y[0], x[1] - y[1] * (x[0] // y[0]), x[2] - y[2] * (x[0] // y[0]))
    return x if m > n else (x[0], x[2], x[1])


def smallest(p1, p2):
    x = euclidean(10 ** len(str(p1)), p2)[1]
    return p1 + 10 ** len(str(p1)) * ((x * p1 * -1) % p2)


def sum_smallest():
    primes = gen_primes(10 ** 6 + 4)
    tot = 0
    for i in range(2, len(primes) - 1):
        tot += smallest(primes[i], primes[i + 1])
    return tot
