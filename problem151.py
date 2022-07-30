from fractions import Fraction


was = {}


def expected(arr):
    if arr[1:].count(0) == len(arr) - 1:
        return 0
    elif tuple(arr) in was:
        return was[tuple(arr)]
    x = 0
    n = sum(arr)
    for i in range(len(arr)):
        if arr[i] != 0:
            a = arr.copy()
            for j in range(i):
                a[j] += 1
            a[i] -= 1
            x += Fraction(arr[i], n) * expected(a)
    if n == 1:
        x += 1
    was[tuple(arr)] = x
    return x
