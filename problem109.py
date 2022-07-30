from itertools import product, combinations_with_replacement


class Hit:
    def __init__(self, region: int, multiple: int):
        self.region = region
        self.multiple = multiple

    def __hash__(self) -> int:
        return self.multiple + 3 * self.region

    def __repr__(self) -> str:
        return f"Hit({self.region}, {self.multiple})"

    def __int__(self) -> int:
        return self.region * self.multiple


def checkouts() -> int:
    all_possible_hits = [Hit(region, multiple) for region, multiple in product(range(1, 21), range(1, 4))]
    all_possible_hits += [Hit(25, 1), Hit(25, 2)]
    one_dart_possible_checkouts = len(list(range(1, 21)) + [25])
    two_dart_possible_checkouts = one_dart_possible_checkouts * len(all_possible_hits)
    two_dart_possible_checkouts -= 1  # 20T -> 20D
    two_dart_possible_checkouts -= 1  # 25D -> 25D
    two_dart_possible_checkouts -= 4  # 17-20D -> 25D
    three_darts_possible_checkouts = 0
    for final_region in list(range(1, 21)) + [25]:
        final_hit = Hit(final_region, 2)
        for first_hit, second_hit in combinations_with_replacement(all_possible_hits, 2):
            if first_hit.__int__() + second_hit.__int__() + final_hit.__int__() < 100:
                three_darts_possible_checkouts += 1
    return one_dart_possible_checkouts + two_dart_possible_checkouts + three_darts_possible_checkouts


if __name__ == "__main__":
    print(checkouts())
