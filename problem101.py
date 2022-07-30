un = lambda x: sum([(-1 * x) ** i for i in range(11)])


def bop(m, f):
    l = [[f(i) for i in range(1, m + 1)]]
    for i in range(m - 1):
        l.append([])
        for j in range(len(l[i]) - 1):
            l[i + 1].append(l[i][j + 1] - l[i][j])
    l[-1].append(l[-1][0])
    for i in range(m - 1, 0, -1):
        l[i - 1].append(l[i - 1][-1] + l[i][-1])
    return l[0][-1], l


def result():
    return sum([bop(i, un)[0] for i in range(1, 11)])
