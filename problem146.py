def prime_pattern(n):
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(int(n ** 0.5)):
        if primes[i]:
            for j in range(2 * i, n, i):
                primes[j] = False
    tot = 0
    for i in range(int((n - 28) ** 0.5)):
        if primes[i ** 2 + 1] and primes[i ** 2 + 3] and primes[i ** 2 + 7] and primes[i ** 2 + 9] and primes[i ** 2 + 13] and primes[i ** 2 + 27]:
            tot += i
            print(i)
    return tot
