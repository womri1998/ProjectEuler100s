def half(max):
    x = 1
    for y in range(1, max + 1):
        x *= y ** 2
    val = [0, 0]
    for i in range(2, max + 1):
        val.append(x // (i ** 2))
    return ways(x // 2, sum([val[i] for i in range(2, max + 1)]), 2, max, val)


def ways(remainder, remaining, l, h, val):
    if remaining < remainder:
        return 0
    if remaining == remainder:
        return 1
    tot = 0
    for i in range(l, h + 1):
        remaining -= val[i]
        tot += ways(remainder - val[i], remaining, i + 1, h, val)
        if remaining < remaining:
            break
    return tot



