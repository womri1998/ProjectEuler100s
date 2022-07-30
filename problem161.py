was = {}


def int_to_bits(n, min_digits=0):
    bits = []
    while n != 0:
        bits.append(bool(n & 1))
        n >>= 1
    while len(bits) < min_digits:
        bits.append(False)
    return bits


def initialize(n):
    for a in range(2 ** n):
        for b in range(2 ** n):
            for c in range(2 ** n):
                for d in range(2 ** n):
                    was[(int_to_bits(a, n), int_to_bits(b, n), int_to_bits(c, n), int_to_bits(d, n))] = options(int_to_bits(a, n), int_to_bits(b, n), int_to_bits(c, n), int_to_bits(d, n))


# orientations: 1 - **, 2 - **, 3 - * , 4 -  *, 5 - *, 6 - ***
#                   *        *      **      **      *
#                                                   *
def options(a, b, c, d, i):
    if (tuple(a), tuple(b), tuple(c), tuple(d)) in was:
        return was[(tuple(a), tuple(b), tuple(c), tuple(d))]
    n = len(a)
    if n == 0:
        return 1
    if b[i] and not c[i]:
        return 0
    if a[i]:
        return options(a, b, c, d, i + 1)
    count = 0
    if not a[i]:
        if not b[i] and c[i] and d[i]: # orientation 5
            count += options(a[:i] + [True] + a[i + 1:], b[i] + [True] + b[i + 1:], c, d)
        elif not d[i] and i > 0 and not b[i] and c[i] and not b[i - 1] and c[i - 1]: # orientation 4
            count += options(a[:i] + [True] + a[i + 1:], b[:i - 1] + [True] * 2 + b[i + 1:], c, d)
        elif not d[i] and not d[i + 1]:
            if i + 2 < n and not a[i + 1] and not a[i + 2] and b[i] == c[i] and b[i + 1] == c[i + 1] and not d[i + 2]: # orientation 6
                count += options(a[:i] + [True] * 3 + a[i + 3:], b, c, d)
            if i + 1 < n:
                if not a[i + 1] and not b[i] and c[i]: # orientation 1
                    count += options(a[:i] + [True] * 2 + a[i + 2:], b[:i] + [True] + b[i + 1:], c, d)
                if not a[i + 1] and not b[i + 1] and c[i + 1] and b[i] == c[i]: # orientation 2
                    count += options(a[:i] + [True] * 2 + a[i + 2:], b[:i + 1] + [True] + b[i + 2:], c, d)
                if not b[i] and c[i] and not b[i + 1] and c[i + 1]: # orientation 3
                    count += options(a[:i] + [True] + a[i + 1], b[:i] + [True] * 2 + b[i + 2:, c, d])
    was[(tuple(a), tuple(b), tuple(c), tuple(d))] = count
    return count


def trinominoes(a, b, left):
    if left == 0:
        return 1
    n = len(a)
    if left == 1:
        return options(a, b, [False] * n, [False] * n)
    elif left == 2:
        return options(a, b, )
