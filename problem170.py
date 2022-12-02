from functools import cache
from math import factorial
from string import digits
from itertools import permutations, chain, combinations
from typing import Iterable


DIGITS = set(digits)


def powerset(iterable: Iterable) -> Iterable:
    """
    :return: The powerset of the input, but without subsets of length < 2.
    """
    l = list(iterable)
    return chain.from_iterable(combinations(iterable, length) for length in range(2, len(l) + 1))


def is_pandigital(n: str) -> bool:
    return len(n) == 10 and set(n) == DIGITS


def concatenated_product(pandigital: list[int]) -> int:
    """
    :param pandigital: list of integers adding up to a pandigital
    """
    x = pandigital[0]
    result = ""
    for y in pandigital[1:]:
        result += str(x * y)
    return int(result) if is_pandigital(result) else 0


@cache
def number(array: tuple[int, ...]) -> int:
    return sum((10 ** i * array[i] for i in range(len(array))))


def max_concatenated_product(pandigital: tuple[int, ...]) -> int:
    """
    :param pandigital: tuple of the digits 0-9
    """

    if pandigital[0] in (0, 1):
        return 0
    result = 0
    for partition in powerset(list(range(1, 9))):
        partition = (0,) + partition + (9,)
        partitioned_pandigital = [pandigital[0]]
        for i in range(len(partition) - 1):
            partitioned_pandigital.append(number(pandigital[partition[i] + 1: partition[i + 1] + 1]))
        result = max((result, concatenated_product(partitioned_pandigital)))
    return result


def main():
    # print(concatenated_product2([6, 1273, 9854]))
    # print(max(max_concatenated_product(pandigital) for pandigital in permutations(range(10))))
    maximum = 0
    for i, pandigital in enumerate(permutations(range(10))):
        if i % 10000 == 0:
            print(i - factorial(9) * 2)
        current = max_concatenated_product(pandigital)
        if maximum < current:
            maximum = current
    print(maximum)


if __name__ == "__main__":
    main()
