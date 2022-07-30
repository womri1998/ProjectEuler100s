from math import gcd


def options(a, b):
    return int(2 * a + 1 == b or 2 * a - 1 == b) + int(2 * b + 1 == a or 2 * b - 1 == a)


def almost_equilateral():
    total, count, n = 0, 0, 1
    while 2 * n * (n + 1) <= k:
        print(n, 2 * n * (n + 1), count, total)
        m = 1
        while 2 * n * (n + m) <= k and m < n:
            a, b, c = n ** 2 - m ** 2, 2 * n * m, n ** 2 + m ** 2
            if gcd(n, m) == 1 and (n % 2 == 0 or m % 2 == 0):
                pre = count
                count += options(a, b)
                if 2 * a + 1 == c or 2 * a - 1 == c:
                    total += 2 * a + 2 * c
                if 2 * b + 1 == c or 2 * b - 1 == c:
                    total += 2 * b + 2 * c
                if count > pre:
                    print(count)
            m += 1
        n += 1
    return total
