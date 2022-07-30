def exponent_factorial(n, m):
    k = m
    count = 0
    while k <= n:
        count += n // k
        k *= m
    return count


def exponent_choose(n, k, m):
    return exponent_factorial(n, m) - exponent_factorial(k, m) - exponent_factorial(n-k, m)


def max_exponent_choose(n, m):
    return max([exponent_factorial(n, m) - exponent_factorial(k, m) - exponent_factorial(n-k, m) for k in range(n + 1)])


def multiples_of():
    for x in range(200001):
        for y in range(200001 - x):

