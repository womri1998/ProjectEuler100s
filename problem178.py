step = {}


def step_numbers(i, n, zero, nine):
    if n == 0:
        if zero and nine:
            return 1
        else:
            return 0
    if (i, n, zero, nine) in step:
        return step[(i, n, zero, nine)]
    x = 0
    if i < 9:
        x += step_numbers(i + 1, n - 1, zero, nine or i + 1 == 9)
    if i > 0:
        x += step_numbers(i - 1, n - 1, zero or i - 1 == 0, nine)
    step[(i, n, zero, nine)] = x
    return x


def total():
    return sum([step_numbers(i, j, False, i == 9) for i in range(1, 10) for j in range(40)])
