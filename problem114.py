red = {0: 1, 1: 0, 2: 0, 3: 1}
black = {0: 1, 1: 1}


def combinations(n):
    return red_start(n) + black_start(n)


def red_start(n):
    if n in red:
        return red[n]
    else:
        x = sum([black_start(i) for i in range(n - 2)])
        red[n] = x
        return x


def black_start(n):
    if n in black:
        return black[n]
    else:
        x = sum([red_start(i) for i in range(n)])
        black[n] = x
        return x
