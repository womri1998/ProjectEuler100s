def is_square(n):
    x = n // 2
    seen = {x}
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return True


def main():
    for i in range(4, 100000):
        a = i ** 2
        for j in range(3, i):
            c = j ** 2
            f = a - c
            if not is_square(f):
                continue
            k_start = 1 if j % 2 == 1 else 2
            for k in range(k_start, j, 2):
                d = k ** 2
                e = a - d
                b = c - e
                if b <= 0:
                    continue
                if is_square(b) and is_square(e):
                    x = (a + b) // 2
                    y = (e + f) // 2
                    z = (c - d) // 2
                    print(i, j, k, x, y, z, x + y, x - y, x + z, x - z, y + z, y - z, x + y + z)
                    return


if __name__ == "__main__":
    main()
