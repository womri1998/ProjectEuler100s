def iter_squaring(x, y, n):
    res = 1
    i = 1
    j = x % n
    while i <= y:
        if y & i != 0:
            res = mod_mul(res, j, n)
        i *= 2
        j = mod_mul(j, j, n)
    return res


def mod_mul(x, y, n):
    res = 0
    i = 1
    j = x % n
    while i <= y:
        if y & i != 0:
            res += j
            res %= n
        i *= 2
        j *= 2
        j %= n
    return res


def hyperexponentiation(x, y, n):
    res = x
    x %= n
    while y > 1:
        res = iter_squaring(x, res, n)
        y -= 1
    return res
