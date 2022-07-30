def prime_cubes(n):
    primes = []
    for i in range(n):
        primes.append([True, False])
    primes[0][0], primes[1][0] = False, False
    for i in range(int(n ** 0.5)):
        if primes[i][0]:
            for j in range(2 * i, n, i):
                primes[j][0] = False
    i = 1
    while (i + 1) ** 3 - i ** 3 < n:
        j = 1
        while (i + j) ** 3 - i ** 3 < n:
            primes[(i + j) ** 3 - i ** 3][1] = True
            j += 1
        i += 1
    return [i for i in range(n) if primes[i] == [True, True]]
