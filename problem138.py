# def sqrt(n: int) -> int:
#     """
#     :param n: input
#     :return: if n is a perfect square, return sqrt(n), else -1
#     """
#     x = n // 2
#     seen = {x}
#     while x * x != n:
#         x = (x + n // x) // 2
#         if x in seen:
#             return 0
#         seen.add(x)
#     return x
#
#
# def special_triangle_plus(b: int) -> int:
#     return sqrt(5 * b * b // 4 + 2 * b + 1)
#
#
# def special_triangle_minus(b: int) -> int:
#     return sqrt(5 * b * b // 4 - 2 * b + 1)
from math import ceil, floor


def special_triangle_1(m: int, n: int) -> bool:
    return 2 * (m * m - n * n) - 2 * m * n in [1, -1]


def special_triangle_2(m: int, n: int) -> bool:
    return m * m - n * n - 4 * m * n in [1, -1]


def special_triangle(m: int, n: int) -> int:
    return (special_triangle_1(m, n) or special_triangle_2(m, n)) * (m * m + n * n)


def update(found: int, total: int, m: int, x: int) -> tuple[int, int]:
    addition = special_triangle(m, x)
    if addition:
        found += 1
        total += addition
        print(found)
    return found, total


def main():
    found, total, m = 0, 0, 2
    while found != 12:
        n = m * 2 / (1 + 5 ** 0.5)
        x = ceil(n)
        found, total = update(found, total, m, x)
        x = floor(n)
        found, total = update(found, total, m, x)
        n = m * 1 / (2 + 5 ** 0.5)
        x = ceil(n)
        found, total = update(found, total, m, x)
        x = floor(n)
        found, total = update(found, total, m, x)
        m += 1
    print(total)


if __name__ == "__main__":
    main()
