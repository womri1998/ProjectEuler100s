def count_solutions(n):
    sol = [0] * (n + 1)
    i = 1
    while ((i // 3 + 1) * 2 + i) ** 2 - ((i // 3 + 1) + i) ** 2 - i ** 2 <= n:
        d = i // 3 + 1
        while difference(i, d) <= n:
            sol[difference(i, d)] += 1
            d += 1
        i += 3
    i = 2
    while ((i // 3 + 1) * 2 + i) ** 2 - ((i // 3 + 1) + i) ** 2 - i ** 2 <= n:
        d = i // 3 + 1
        while difference(i, d) <= n:
            sol[difference(i, d)] += 1
            d += 1
        i += 3
    i = 3
    while ((i // 3 + 1) * 2 + i) ** 2 - ((i // 3 + 1) + i) ** 2 - i ** 2 <= n:
        d = i // 3 + 1
        while difference(i, d) <= n:
            sol[difference(i, d)] += 1
            d += 1
        i += 3
    return sum([1 for x in sol if x == 1])


def difference(n, d):
    return (n + 2 * d) ** 2 - (n + d) ** 2 - n ** 2
