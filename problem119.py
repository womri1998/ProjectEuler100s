def powers(m):
    n = 10 ** m
    res = {}
    for i in range(2, 9 * m):
        j = i
        while j < n:
            if j not in res:
                res[j] = []
            res[j].append(i)
            j *= i
    return res


def digits_sum(x):
    s = 0
    r = x
    while r:
        s, r = s + r % 10, r // 10
    return s


def sequence(m):
    power = powers(m)
    res = []
    keys = sorted(power.keys())
    for i in keys:
        if i > 10 and digits_sum(i) in power[i]:
            res.append(i)
    return res
