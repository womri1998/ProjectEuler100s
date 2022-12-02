from queue import Queue
from itertools import combinations_with_replacement


def main():
    queue: Queue[tuple[int, list[int]]] = Queue()
    depths = [0, 0] + [100] * 199
    queue.put_nowait((0, [1]))
    while 100 in depths[1:]:
        depth, cache = queue.get_nowait()
        for x, y in combinations_with_replacement(cache, 2):
            n = x + y
            if n > 200:
                continue
            new_cache = cache.copy() + [n]
            new_depth = depth + 1
            if depths[n] == 100:
                depths[n] = new_depth
            if depths[n] == new_depth:
                queue.put_nowait((new_depth, new_cache))
    return sum(depths[1:])


if __name__ == '__main__':
    print(main())
