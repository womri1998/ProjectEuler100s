import math


def n_choose_k(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def bouncy_numbers(n):
    return n_choose_k(9 + n, 9) + n_choose_k(10 + n, 10) - 10 * n - 2
