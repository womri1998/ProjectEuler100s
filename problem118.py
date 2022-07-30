from itertools import permutations
from useful import gen_primes


primes = gen_primes(10 ** 7)
pandigital_primes = [p for p in primes if '0' not in str(p) and True not in [str(p).count(str(i)) > 1 for i in range(1, 10)]]
was = {}


def is_prime(n):
    if n < 10 ** 7:
        return n in pandigital_primes
    else:
        for p in primes:
            if n % p == 0:
                return False
            if p > n ** 0.5:
                return True
    return -1


def digits_to_int(digits):
    return sum([digits[-1 - i] * 10 ** i for i in range(len(digits))])


def total_goods():
    count = 0
    for p in permutations([i for i in range(1, 10)]):
        if is_prime(digits_to_int(p)):
            count += 1
    for x in gen_primes(10):
        for p in permutations([i for i in range(1, 10) if i != x]):
            if is_prime(digits_to_int(p)):
                count += 1
    print("wut", count)
    return count + good_partitions([True] * 9, 10 ** 7)


def good_partitions(left, below):
    if True not in left:
        return 1
    if (tuple(left), below) in was:
        return was[(tuple(left), below)]
    count = 0
    for p in pandigital_primes:
        if p >= below:
            break
        new_left = left.copy()
        good = True
        for c in str(p):
            if not left[int(c) - 1]:
                good = False
                break
            else:
                new_left[int(c) - 1] = False
        if good:
            count += good_partitions(new_left, p)
    was[(tuple(left), below)] = count
    return count
