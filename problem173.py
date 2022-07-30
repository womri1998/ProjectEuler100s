def count(n):
    count = 0
    i = 2
    while i ** 2 - (i - 2) ** 2 <= n:
        j = 2
        while i ** 2 - (i - j) ** 2 <= n and i > j:
            count += 1
            j += 2
        i += 2
    i = 3
    while i ** 2 - (i - 2) ** 2 <= n:
        j = 2
        while i ** 2 - (i - j) ** 2 <= n and i > j:
            count += 1
            j += 2
        i += 2
    return count
