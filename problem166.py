def first():
    count = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    print(a, b, c, d)
                    count += second([[a, b, c, d]])
    return count


def second(cur):
    count = 0
    n = sum(cur[0])
    for a in range(10):
        for b in range(10):
            for c in range(10):
                d = n - a - b - c
                if 0 <= d < 10:
                    count += third(cur + [[a, b, c, d]])
    return count


def third(cur):
    count = 0
    n = sum(cur[0])
    for a in range(10):
        b = cur[0][0] + cur[1][0] + a - cur[0][3] - cur[1][2]
        if 0 <= b < 10:
            for c in range(10):
                d = cur[0][0] + cur[1][1] + c - cur[0][3] - cur[1][3]
                if 0 <= d < 10 and a + b + c + d == n:
                    count += fourth(cur + [[a, b, c, d]])
    return count


def fourth(cur):
    n = sum(cur[0])
    a = n - cur[0][0] - cur[1][0] - cur[2][0]
    b = n - cur[0][1] - cur[1][1] - cur[2][1]
    c = n - cur[0][2] - cur[1][2] - cur[2][2]
    d = n - cur[0][3] - cur[1][3] - cur[2][3]
    return a + b + c + d == n and 0 <= a < 10 and 0 <= b < 10 and 0 <= c < 10 and 0 <= d < 10

    #return a + b + c + d == n
    #cur = cur + [[a, b, c , d]]
    #if sum(cur[1]) != n or sum(cur[2]) != n or sum(cur[3]) != n or cur[0][0] + cur[1][1] + cur[2][2] + cur[3][3] != n or \
    #    cur[0][3] + cur[1][2] + cur[2][1] + cur[3][0] != n or cur[0][0] + cur[1][0] + cur[2][0] + cur[3][0] != n or \
    #    cur[0][1] + cur[1][1] + cur[2][1] + cur[3][1] != n or cur[0][2] + cur[1][2] + cur[2][2] + cur[3][2] != n or \
    #    cur[0][3] + cur[1][3] + cur[2][3] + cur[3][3] != n:
    #    for i in range(len(cur)):
    #        print(cur[i])
    #    print()
    #bad = False
    #for x in cur:
    #    for y in x:
    #        if y < 0 or y >= 10:
    #            bad = True
    #if bad:
    #    for i in range(len(cur)):
    #        print(cur[i])
