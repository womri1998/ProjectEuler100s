from math import tan, atan


def incline(x1, y1, x2, y2):
    return (y1 - y2) / (x1 - x2)


def tangent_slope(x, y):
    return -4 * x / y


def next_incline(m, x, y):
    m2 = tangent_slope(x, y)
    return tan(2 * atan(m2) - atan(m))


def next_conf(m, x, y):
    m = next_incline(m, x, y)
    n = y - m * x
    x1 = (-1 * m * n + (m ** 2 * n ** 2 + (100 - n ** 2) * (m ** 2 + 4)) ** 0.5) / (m ** 2 + 4)
    x2 = (-1 * m * n - (m ** 2 * n ** 2 + (100 - n ** 2) * (m ** 2 + 4)) ** 0.5) / (m ** 2 + 4)
    if abs(x1 - x) < abs(x2 - x):
        x = x2
    else:
        x = x1
    y = m * x + n
    return m, x, y


def reflections():
    count = 0
    m, x, y = incline(0, 10.1, 1.4, -9.6), 1.4, -9.6
    while abs(x) > 0.01 or y < 0:
        m, x, y = next_conf(m, x, y)
        print(count, m, x, y)
        count += 1
    return count
