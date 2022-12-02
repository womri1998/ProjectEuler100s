from collections import defaultdict
from typing import Generator
from itertools import product
from fractions import Fraction


def series(capacitors: list[Fraction]) -> Fraction:
    return Fraction(1, sum(Fraction(1, capacitor) for capacitor in capacitors))


def parallel(capacitors: list[Fraction]) -> Fraction:
    return sum(capacitors)


def partitions(n: int, i: int = 1) -> Generator[tuple[int, ...], None, None]:
    yield (n,)
    for j in range(i, n // 2 + 1):
        for p in partitions(n - j, j):
            yield (j,) + p


def d(n: int):
    seen: set[Fraction] = {Fraction(1)}
    values_by_amount: dict[int, list[Fraction]] = defaultdict(lambda: [])
    values_by_amount[1] = [Fraction(1)]
    for i in range(2, n + 1):
        print(i)
        for partition in partitions(i):
            for capacitors in product(*(values_by_amount[x] for x in partition)):
                new_series = series(capacitors)
                if new_series not in seen:
                    seen.add(new_series)
                    values_by_amount[i].append(new_series)
                new_parallel = parallel(capacitors)
                if new_parallel not in seen:
                    seen.add(new_parallel)
                    values_by_amount[i].append(new_parallel)
    return len(seen)


def main():
    print(d(18))


if __name__ == "__main__":
    main()
