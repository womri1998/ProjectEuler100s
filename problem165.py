from fractions import Fraction


s = [290797 ** 2 % 50515093]
for i in range(1, 20000):
    s.append(s[-1] ** 2 % 50515093)

points = [(s[i] % 500, s[i + 1] % 500) for i in range(0, len(s), 2)]


def slope(p1, p2):
    if p1[0] - p2[0] == 0:
        return None  # i.e. always x = const
    return Fraction(p1[1] - p2[1], p1[0] - p2[0])


def n_of_line(m, x):
    if m is None:
        return None
    return x[1] - m * x[0]


lines = [(points[i], points[i + 1], slope(points[i], points[i + 1]), n_of_line(slope(points[i], points[i + 1]), points[i])) for i in range(0, len(points), 2)]


def intersection(l1, l2):
    if l1[2] == l2[2]:
        return None, None
    elif l1[2] is None:
        return l1[0][0], l2[2] * l1[0][0] + l2[3]
    elif l2[2] is None:
        return l2[0][0], l1[2] * l2[0][0] + l1[3]
    else:
        x = Fraction(l1[3] - l2[3], l2[2] - l1[2])
        return x, x * l1[2] + l1[3]


was = set({})


def true_intersection(l1, l2):
    x, y = intersection(l1, l2)
    if x is None:
        return
    elif l2[2] is None:
        if (l1[0][0] < x < l1[1][0] or l1[0][0] > x > l1[1][0]) and (l2[0][1] < y < l2[1][1] or l2[0][1] > y > l2[1][1]):
            was.add((x, y))
    elif l1[2] is None:
        if (l1[0][1] < y < l1[1][1] or l1[0][1] > y > l1[1][1]) and (l2[0][0] < x < l2[1][0] or l2[0][0] > x > l2[1][0]):
            was.add((x, y))
    else:
        if (l1[0][0] < x < l1[1][0] or l1[0][0] > x > l1[1][0]) and (l2[0][0] < x < l2[1][0] or l2[0][0] > x > l2[1][0]):
            was.add((x, y))


for i in range(len(lines)):
    print(i)
    for j in range(i + 1, len(lines)):
        true_intersection(lines[i], lines[j])


print(len(was))

# 2868868
