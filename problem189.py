was_lower = {}
was_upper = {}


def lower(last, cur, length):
    if len(cur) == length:
        return 1
    elif len(cur) > len(last):
        return upper(tuple(cur), [], length)
    elif (last, tuple(cur), length) in was_lower:
        return was_lower[(last, tuple(cur), length)]
    x = 0
    if len(cur) == 0:
        for i in range(3):
            x = sum([lower(last, [j], length) for j in range(3) if j != last[0]])
    elif len(cur) == len(last):
        for i in range(3):
            x = sum([lower(last, cur + [j], length) for j in range(3) if j != last[-1]])
    else:
        for i in range(3):
            x = sum([lower(last, cur + [j], length) for j in range(3) if j != last[len(cur)] and j != last[len(cur) - 1]])
    was_lower[(last, tuple(cur), length)] = x
    return x


def upper(last, cur, length):
    if len(cur) == len(last):
        return lower(tuple(cur), [], length)
    elif (last, tuple(cur), length) in was_upper:
        return was_upper[(last, tuple(cur), length)]
    x = sum([upper(last, cur + [i], length) for i in range(3) if i != last[len(cur)]])
    was_upper[(last, tuple(cur), length)] = x
    return x


def total():
    return sum([lower([], [i], 8) for i in range(3)])
