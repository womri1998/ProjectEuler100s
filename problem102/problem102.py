def same_as_origin(l, a):
    if type(l) == int:
        return (a[0] < l and 0 <= l) or (a[0] > l and 0 >= l)
    return (l[0] * a[0] + l[1] < a[1] and l[1] <= 0) or (l[0] * a[0] + l[1] > a[1] and l[1] >= 0)


def get_line(a, b):
    if a[0] == b[0]:
        return a[0]
    m = (a[1] - b[1]) / (a[0] - b[0])
    n = a[1] - m * a[0]
    return (m, n)


def contains_origin(triangle):
    points = [(triangle[0], triangle[1]), (triangle[2], triangle[3]), (triangle[4], triangle[5])]
    lines = [get_line(points[0], points[1]), get_line(points[0], points[2]), get_line(points[1], points[2])]
    return same_as_origin(lines[0], points[2]) and same_as_origin(lines[1], points[1]) and same_as_origin(lines[2], points[0])


def count_origins(file):
    f = open(file, 'r')
    txt = f.read().splitlines()
    triangles = [line.split(',') for line in txt]
    for t in triangles:
        for i in range(len(t)):
            t[i] = int(t[i])
        print(t)
    print(sum([contains_origin(t) for t in triangles]))
    f.close()


if __name__ == "__main__":
    count_origins("p102_triangles.txt")
