from itertools import combinations


def sum_free(s):
    a = list(s)
    for i in range(1, len(a) + 1):
        for j in range(1, len(a) + 1):
            for x in combinations(a, i):
                for y in combinations(a, j):
                    if (x != y and sum(x) == sum(y)) or (i > j and sum(x) < sum(y)):
                        return False
    return True


def best(n, s):
    res = n ** 3 + 100
    cur_best = s.union({100000})
    if len(s) == 0:
        for i in range(1, int(2 * 2 ** (n / 2))):
            x = best(n, {i})
            if x[0] < res:
                res = x[0]
                cur_best = x[1]
        return res, cur_best
    if len(s) == n:
        return sum(s), s
    i = max(s) + 1
    s_sum = sum(s)
    s_len = len(s)
    while s_sum + i * (n - s_len) + s_len * (s_len + 1) // 2 < 2 ** n:
        x = best(n, s.union({i}))
        if x[0] < res:
            res = x[0]
            cur_best = x[1]
        i += 1
    return res, cur_best
