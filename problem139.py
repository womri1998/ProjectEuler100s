def gcd(m, n):
    x = max(m, n)
    y = min(m, n)
    while y != 0:
        x, y = y, x % y
    return x


def pythagorean_tiles(k):
    count, n = 0, 1
    while 2 * (n + 1) ** 2 + 2 * n * (n + 1) < k:
        m = 1
        while 2 * (n + m) ** 2 + 2 * n * (n + m) < k:
            if gcd(n, n + m) == 1 and (n % 2 == 0 or (n + m) % 2 == 0) and ((n + m) ** 2 + n ** 2) % ((n + m) ** 2 - n ** 2 - 2 * n * (n + m)) == 0:
                count += k // (2 * (n + m) ** 2 + 2 * n * (n + m))
            m += 1
        n += 1
    return count
