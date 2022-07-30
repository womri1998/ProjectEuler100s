comb = {0: 1}
def combinations(n):
    if n < 0:
        return 0
    elif n in comb:
        return comb[n]
    else:
        if not n - 1 in comb:
            comb[n - 1] = combinations(n - 1)
        return sum([comb[i] for i in range(max(n - 4, 0), n)])
