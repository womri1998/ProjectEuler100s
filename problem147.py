def copies(x: int, y: int, n: int, m: int) -> int:
    return (n - x + 1) * (m - y + 1)


def main():
    n = 3
    m = 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(i, j, copies(i, j, n, m))


if __name__ == "__main__":
    main()
