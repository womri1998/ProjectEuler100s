from queue import SimpleQueue as Queue
from typing import Iterable
from itertools import combinations_with_replacement


def is_dict_full(d: dict, wanted_keys: Iterable) -> bool:
    return all([key in d for key in wanted_keys])


def bfs() -> int:
    past_states: set[frozenset[int]] = set()
    states: Queue[tuple[frozenset[int], int]] = Queue()
    states.put((frozenset([1]), 1))
    most_efficient: dict[int] = dict()
    most_efficient[1] = 1
    while not is_dict_full(most_efficient, range(1, 201)):
        state, steps = states.get()
        past_states.add(state)
        for exp1, exp2 in combinations_with_replacement(state, 2):
            new_exp = exp1 + exp2
            if new_exp > 200:
                break
            if new_exp not in most_efficient or most_efficient[new_exp] > steps + 1:
                most_efficient[new_exp] = steps + 1
            new_state = set(state)
            new_state.add(new_exp)
            if new_state not in past_states:
                states.put((frozenset(new_state), steps + 1))
    return sum([most_efficient[key] for key in range(1, 201)])


if __name__ == "__main__":
    print(bfs())
