import math


def count(n, m, k):
    return math.factorial(16) // math.factorial(n) // math.factorial(m) // math.factorial(k) // math.factorial(16 - n - m - k)* 13 ** (16 - n - m - k)


def total():
    tot = 0
    for i in range(1, 17):
        for j in range(1, 17 - i):
            for k in range(1, 17 - i - j):
                tot += count(i, j, k)
                print(i, j, k)
    return tot


def n_choose_k(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


def total2():
    tot = 0
    for n in range(3, 17):
        tot += 15 * (16 ** (n - 1)) - 43 * (15 ** (n - 1)) + 41 * (14 ** (n - 1)) - 13 ** n
    return tot
