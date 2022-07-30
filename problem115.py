def combinations(n, m):
    global red
    global black
    red = {0: 1, m: 1}
    for i in range(1, m):
        red[i] = 0
    black = {0: 1, 1: 1}
    return red_start(n, m) + black_start(n, m)


def red_start(n, m):
    global red
    global black
    if n in red:
        return red[n]
    else:
        x = sum([black_start(i, m) for i in range(n - m + 1)])
        red[n] = x
        return x


def black_start(n, m):
    global red
    global black
    if n in black:
        return black[n]
    else:
        x = sum([red_start(i, m) for i in range(n)])
        black[n] = x
        return x
