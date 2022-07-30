def gcd(m, n):
    x, y = max(m, n), min(m, n)
    while y != 0:
        x, y = y, x % y
    return x


def solutions(n):
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if (i * n) % (i - n) == 0:
            print(i, (i * n) // (i - n))
            count += 1
    return count


def first_above(n):
    i = 1
    while solutions(i) < n:
        i += 1
        if i % 1000 == 0:
            print(i)
    return i


def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(int(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]
