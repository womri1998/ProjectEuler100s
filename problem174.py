def count(n, m):
    was = [0] * (n + 1)
    i = 2
    while i ** 2 - (i - 2) ** 2 <= n:
        j = 2
        while i ** 2 - (i - j) ** 2 <= n and i > j:
            was[i ** 2 - (i - j) ** 2] += 1
            j += 2
        i += 2
    i = 3
    while i ** 2 - (i - 2) ** 2 <= n:
        j = 2
        while i ** 2 - (i - j) ** 2 <= n and i > j:
            was[i ** 2 - (i - j) ** 2] += 1
            j += 2
        i += 2
    count = 0
    for x in was:
        if 0 < x <= m:
            count += 1
    return count
