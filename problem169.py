was = {}


def options(n):
    was.clear()
    pos = []
    i = 0
    while n // 2 ** i != 0:
        pos.append(min(2, n // 2 ** i))
        i += 1
    return ways(n, pos)


def ways(n, pos):
    if (n, tuple(pos)) in was:
        return was[(n, tuple(pos))]
    elif n == 0:
        return 1
    elif n < 0 or sum([pos[i] * 2 ** i for i in range(len(pos))]) < n:
        return 0
    else:
        res = 0
        for i in range(len(pos)):
            if pos[i] == 2:
                res += ways(n - 2 ** i, pos[:i] + [1])
            elif pos[i] == 1:
                res += ways(n - 2 ** i, pos[:i])
        was[(n, tuple(pos))] = res
        return res
