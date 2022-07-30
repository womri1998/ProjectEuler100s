from fractions import Fraction


def cycle(n):
    a, m, d = int(n ** 0.5), 0, 1
    was = [(a, m, d)]
    m = a * d - m
    d = (n - m ** 2) / d
    a = int((n ** 0.5 + m) / d)
    while (a, m, d) not in was:
        was.append((a, m, d))
        m = a * d - m
        d = (n - m ** 2) / d
        a = int((n ** 0.5 + m) / d)
    return [was[i][0] for i in range(len(was) - 1)]


def basic(v):
    return v[0] + conv(v[1:])


def conv(v):
    if len(v) == 0:
        return 0
    else:
        return Fraction(1, v[0] + conv(v[1:]))


def next(x, b, n):
    return x[0] * b[0] + n * x[1] * b[1], x[0] * b[1] + x[1] * b[0]


def min(n):
    x = basic(cycle(n)).numerator, basic(cycle(n)).denominator
    return x


# goal: solve (5n - 1) ** 2 - 5 * y ** 2 = 4
# x ** 2 - 5 * y ** 2 = 4 basic solutions:
b1 = 4, 2
b2 = 11, 5
b3 = 29, 13
# x ** 2 - 5 * y ** 2 = 1 basic solution:
b = 9, 4



def golden_nugget(n):
    count = 0
    x1, x2, x3 = b1, b2, b3
    while True:
        if x1[0] % 5 == 1:
            count += 1
            print(x1[0], count)
            if count == n:
                return (x1[0] + 1) // 5
        if x2[0] % 5 == 1:
            count += 1
            print(x2[0], count)
            if count == n:
                return (x2[0] + 1) // 5
        if x3[0] % 5 == 1:
            count += 1
            print(x3[0], count)
            if count == n:
                return (x3[0] + 1) // 5
        x1 = next(x1, b, 5)
        x2 = next(x2, b, 5)
        x3 = next(x3, b, 5)
