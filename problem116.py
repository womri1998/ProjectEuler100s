comb = {}
def combinations(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif (n, m) in comb:
        return comb[n, m]
    else:
        if (n - 1, m) in comb:
            x = comb[n - 1, m]
        else:
            x = combinations(n - 1, m)
            comb[n - 1, m] = x
        if (n - m, m) in comb:
            y = comb[n - m, m]
        else:
            y = combinations(n - m, m)
            comb[n - m, m] = y
        return x + y
