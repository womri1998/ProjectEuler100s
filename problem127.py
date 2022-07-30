def gen_primes(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(int(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    return [i for i in range(n) if primes[i]]


primes = gen_primes(120000)


def gcd(m, n):
    x, y = max(m, n), min(m, n)
    while y != 0:
        x, y = y, x % y
    return x


def radical(n):
    res = 1
    i = 0
    while n != 1:
        if n % primes[i] == 0:
            res *= primes[i]
        while n % primes[i] == 0:
            n //= primes[i]
        i += 1
    return res


def abc_hits2(n):
    count, tot = 0, 0
    for i in range(1, n // 2):
        for j in range(1, n - 2 * i):
            if gcd(i, i + j) == 1 and radical(i * (i + j) * (2 * i + j)) < 2 * i + j:
                count += 1
                tot += 2 * i + j
                print(i, i + j, 2 * i + j, radical(i * (i + j) * (2 * i + j)))
    return count, tot


def radicals(n):
    res = [0]
    for i in range(n):
        res += [[1, []]]
    primes = gen_primes(n)
    print(961 in primes)
    for p in primes:
        for i in range(p, len(res), p):
            res[i][0] *= p
            res[i][1].append(p)
    return res


def abc_hits(n):
    count, tot = 0, 0
    rad = radicals(n)
    for i in range(1, n // 2):
        gcd1 = [False] + [True] * n
        for p in rad[i][1]:
            for j in range(p, n + 1, p):
                gcd1[j] = False
        for j in range(i + 1, n + 1 - i):
            if gcd1[j] and rad[i][0] * rad[j][0] * rad[i + j][0] < i + j:
                count += 1
                tot += i + j
                print(i, j, i + j, rad[i][0] * rad[j][0] * rad[i + j][0])
            if i == 1 and j == 960:
                print(i, j, i + j, rad[i], rad[j], rad[i + j], "what???")
    return count, tot
