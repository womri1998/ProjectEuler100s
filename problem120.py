def gcd(a, b):
    x = max(a, b)
    y = min(a, b)
    while y != 0:
        x, y = y, x % y
    return x


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


def cycle(x, n):
    y = x
    count = 1
    while y != 1:
        y = mod_mul(y, x, n)
        count += 1
    return count


def lcm(x, y):
    return x * y // gcd(x, y)


def best_remainder(a):
    best = 2
    x, y = a - 1, a + 1
    for i in range(lcm(cycle(a - 1, a ** 2), cycle(a + 1, a ** 2))):
        if (x + y) % a ** 2 > best:
            best = (x + y) % a ** 2
        x = mod_mul(x, a - 1, a ** 2)
        y = mod_mul(y, a + 1, a ** 2)
    return best


def total(n):
    return sum([best_remainder(i) for i in range(3, n + 1)])
