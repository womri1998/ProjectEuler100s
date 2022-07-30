from Pell import gen_basic_solutions, basic_solution, next


a, b = (7 * 5 ** 0.5 + 5) / 10, (5 - 7 * 5 ** 0.5) / 10
phi, psi = (1 + 5 ** 0.5) / 2, (1 - 5 ** 0.5) / 2


def g(n):
    return a * phi ** n + b * psi ** n


def ag(x):
    return a * x / (1 - phi * x) + b * x / (1 - psi * x)


def ag2(x):
    return (x + 3 * x ** 2) / (1 - x - x ** 2)


# final equation: (5 * n + 7) ** 2 - 5 * m ** 2 = 44
# x ** 2 - 5 * y ** 2 = 44 basic solution = (7, 1)
# x ** 2 - 5 * y ** 2 = 1 basic solution: (9, 4)


def golden_nuggets(n, d, k):
    res = 0
    count = 0
    x = gen_basic_solutions((7, 1), (9, 4), d, k)
    print(x)
    while True:
        for y in x:
            if y[0] % 5 == 2:
                count += 1
                res += (y[0] - 7) / 5
                print(y, count, (y[0] - 7) / 5)
                if count == n + 1:
                    return res
        x = [next(y, basic_solution(d), d) for y in x]
