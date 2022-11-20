from math import ceil

LIMIT = int(1e6)


def digit_sum(n: int) -> int:
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
    return total


def digital_root(n: int) -> int:
    while n >= 10:
        n = digit_sum(n)
    return n


def generate_mdrs(limit: int) -> list[int]:
    mdrs = [0] * limit
    for factor in range(2, limit):
        for original in range(1, ceil(limit / factor)):
            mdrs[original * factor] = max((mdrs[original * factor], mdrs[original] + digital_root(factor)))
    return mdrs


def main():
    print(sum(generate_mdrs(LIMIT)[2:]))


if __name__ == "__main__":
    main()
