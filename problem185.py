from copy import deepcopy
from itertools import combinations
from string import digits
from typing import Optional

GUESSES = """5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct"""


EXAMPLE = """90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct"""


def parse_input(s: str) -> list[tuple[str, int]]:
    lines = s.split('\n')
    guesses = []
    for line in lines:
        guess, correct = line.split(';')
        guess, correct = guess.strip(), int(correct.split()[0])
        guesses.append((guess, correct))
    return guesses


def final_solution(options: list[set[str]]) -> bool:
    return all([len(digit_options) == 1 for digit_options in options])


def valid_solution(options: list[set[str]]) -> bool:
    return all(options)


def find_solutions(n: int, guesses: list[tuple[str, int]], options: list[set[str]], index: int):
    guess, correct = guesses[index]
    for combination in combinations(range(n), correct):
        new_options = deepcopy(options)
        for i in range(n):
            if i in combination:
                new_options[i].intersection_update({guess[i]})
            else:
                new_options[i].discard(guess[i])
        if valid_solution(new_options):
            if final_solution(new_options) and index == n:
                print(new_options)
            else:
                find_solutions(n, guesses, new_options, index + 1)


def print_unique_solution(n: int, guesses: list[tuple[str, int]]):
    options = [{digit for digit in digits} for _ in range(n)]
    find_solutions(n, guesses, options, 0)


def main():
    guesses = parse_input(GUESSES)
    example = parse_input(EXAMPLE)
    print_unique_solution(len(example[0][0]), example)
    print_unique_solution(len(guesses[0][0]), guesses)


if __name__ == "__main__":
    main()