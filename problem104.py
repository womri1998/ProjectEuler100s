from math import log


def fibonacci_head(n):
    return int(10 ** ((n * log((1 + 5 ** 0.5) / 2, 10) - log(5 ** 0.5, 10)) % 1 + 8))


def pandigital(n):
    n = str(n)
    for i in range(49, 58):
        if chr(i) not in n:
            return False
    return True


def find():
    x, y, i = 1, 1, 2
    while True:
        x, y = (x + y) % (10 ** 9), x
        if pandigital(y) and pandigital(fibonacci_head(i)):
            print(y, fibonacci_head(i))
            return i
        i += 1
        if i == 10 ** 6:
            print('blyat')
