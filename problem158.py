was = {}


def count(last, left, length, lex):
    if length == 0:
        if lex:
            return 1
        else:
            return 0
    elif (last, left, length, lex) in was:
        return was[(last, left, length, lex)]
    x = 0
    for i in range(last, left):
        x += count(i, left - 1, length - 1, lex)
    if not lex:
        for i in range(last):
            x += count(i, left - 1, length - 1, True)
    was[(last, left, length, lex)] = x
    return x


def p(n):
    return count(0, 26, n, False)


def res():
    return max([p(i) for i in range(1, 27)])
