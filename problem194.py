from itertools import product
from math import factorial


TYPE_A = 0
TYPE_B = 2
COLORS = 4
# TYPE_A = 25
# TYPE_B = 75
# COLORS = 1984
MODULO = 10 ** 8
TYPE_A_EDGES = {(0, 1), (0, 2), (0, 5), (1, 0), (1, 4), (1, 6), (2, 0), (2, 3), (2, 5), (3, 2), (3, 4), (4, 1), (4, 3),
                (4, 6), (5, 0), (5, 2), (5, 6), (6, 1), (6, 4), (6, 5)}
TYPE_B_EDGES = {edge for edge in TYPE_A_EDGES}
TYPE_B_EDGES.remove((1, 6))
TYPE_B_EDGES.remove((6, 1))


def modulo_multiply(x: int, y: int) -> int:
    return x * y % MODULO


def skipped_color(coloring: list) -> bool:
    last = max(coloring)
    for i in range(last):
        if i not in coloring:
            return True
    return False


def calculate_graph_multiplicand(colors: int, graph: set) -> int:
    total = 0
    for coloring in [element for element in product([0], [1], *[[x for x in range(7)] for i in range(5)]) if max(element) < colors]:
        same = set()
        for x in range(len(coloring)):
            for y in range(len(coloring)):
                if x != y and coloring[x] == coloring[y]:
                    same.add((x, y))
        if set.isdisjoint(same, graph) and not skipped_color(coloring):
            new_colors = max(coloring) - 1
            choosing_colors_options = 1
            for i in range(new_colors):
                choosing_colors_options *= colors - 2 - i
            total += choosing_colors_options
            print(coloring, choosing_colors_options)
    return total


def calculate_a_multiplicand(colors: int) -> int:
    return calculate_graph_multiplicand(colors, TYPE_A_EDGES)


def calculate_b_multiplicand(colors: int) -> int:
    return calculate_graph_multiplicand(colors, TYPE_B_EDGES)


def configurations(type_a: int, type_b: int, colors: int) -> int:
    units_order_multiplicand = factorial(TYPE_A + TYPE_B) // factorial(TYPE_A) // factorial(TYPE_B)
    starting_colors_multiplicand = COLORS * (COLORS - 1)
    # type_a_multiplicand = calculate_a_multiplicand(colors)
    type_b_multiplicand = calculate_b_multiplicand(colors)
    print(units_order_multiplicand, starting_colors_multiplicand, type_b_multiplicand)
    result = units_order_multiplicand % MODULO
    result = modulo_multiply(result, starting_colors_multiplicand)
    for i in range(type_a):
        result = modulo_multiply(result, type_a_multiplicand)
    for i in range(type_b):
        result = modulo_multiply(result, type_b_multiplicand)
    return result


if __name__ == "__main__":
    print(configurations(TYPE_A, TYPE_B, COLORS))
