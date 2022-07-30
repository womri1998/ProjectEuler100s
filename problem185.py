from itertools import combinations


input = [(5616185650518293, 2), (3847439647293047 , 1), (5855462940810587, 3), (9742855507068353, 3), (4296849643607543, 3), (3174248439465858, 1),
        (4513559094146117, 2), (7890971548908067, 3), (8157356344118483, 1), (2615250744386899, 2), (8690095851526254, 3), (6375711915077050, 1),
        (6913859173121360, 1), (6442889055042768, 2), (2321386104303845, 0), (2326509471271448, 2), (5251583379644322, 2), (1748270476758276, 3),
        (4895722652190306, 1), (3041631117224635, 3), (1841236454324589, 3), (2659862637316867, 2)]


def int_to_digits(n):
    d = []
    while n != 0:
        d.append(n % 10)
        n //= 10
    return d


def digits_to_int(d):
    n = 0
    for i in range(len(d)):
        n += d[i] * 10 ** i
    return n


guesses = [(int_to_digits(input[i][0]), input[i][1]) for i in range(len(input))]


def apply(guess, cur, comb):
    new = cur.copy()
    for x in comb:
        new[x] = guess[x]
    return new


def left_to_guess(next, cur):
    left = next[1]
    nones = 0
    for i in range(len(cur)):
        if cur[i] is None:
            nones += 1
        if cur[i] == next[0][i]


def search(left, cur):
    if len(left) == 0:
        return digits_to_int(cur)
    not_guessed = [i for i in range(len(cur)) if cur[i] is None]
    for comb in combinations(not_guessed, left[0][1]):
        res = search(left[1:], apply(left[0][0], cur, comb))
        if res != 0:
            return res
    return 0
