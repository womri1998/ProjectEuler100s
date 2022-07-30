def f(x):
    return int(2 ** (30.403243784 - x ** 2)) * 10 ** -9


def u(n):
    res = -1
    for i in range(n):
        res = f(res)
    return res
