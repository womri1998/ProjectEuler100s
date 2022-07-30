import math


was = {}


def arrangements(arr):
    if arr in was:
        return was[arr]
    x = math.factorial(sum(arr))
    for y in arr:
        x //= math.factorial(y)
    was[arr] = x
    return x


def choose(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)


def count(used, i):
    if sum(used) == 18:
        return choose(17, used[0]) * arrangements(tuple(sorted(used[1:])))
    elif i == 10:
        return 0
    res = 0
    if used[i] < 3:
        u = used.copy()
        u[i] += 1
        res += count(u, i)
    res += count(used, i + 1)
    return res
