import math


was = {}


def chance(blue, cur, tot):
    if cur == tot:
        if blue > (tot - 1) // 2:
            return 1
        else:
            return 0
    if (blue, cur, tot) in was:
        return was[(blue, cur, tot)]
    x = chance(blue + 1, cur + 1, tot) + cur * chance(blue, cur + 1, tot)
    was[(blue, cur, tot)] = x
    return x


def max_prize():
    return (math.factorial(16) - chance(0, 1, 16)) // chance(0, 1, 16)
