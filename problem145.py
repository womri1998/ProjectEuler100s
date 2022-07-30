import math


def reverse(n):
    return int(str(n)[::-1])


def reversible(n):
    if n % 10 == 0:
        return False
    m = str(n + reverse(n))
    for c in m:
        if int(c) % 2 == 0:
            return False
    return True


def count_reversibles(n):
    count = 0
    for i in range(n):
        if reversible(i):
            count += 1
    return count


def count_reversibles2(digits):
    return sum([count_reversibles3(i) for i in range(2, digits + 1)])


def count_reversibles3(digits):
    tot = 0
    for i in range(2 ** (math.ceil(digits / 2) * 2)):
        even = int_to_bytes(i % 2 ** math.ceil(digits / 2), math.ceil(digits / 2))
        carry = int_to_bytes(i // 2 ** math.ceil(digits / 2), math.ceil(digits / 2))
        tot += count_reversibles4(even, carry, digits)
    return tot


def int_to_bytes(n, digits):
    bytes = []
    while n != 0:
        bytes.append(n % 2)
        n //= 2
    while len(bytes) < digits:
        bytes.append(0)
    return bytes[::-1]

def count_reversibles4(even, carry, digits):
    n = 0
    for i in range(len(even)):
        if carry[i] == 0:
            n += (even[i] + 3) * 10 ** i
        else:
            n += (even[i] + 7) * 10 ** i
    i += 1
    while i < digits:
        n += 4 * 10 ** i
        i += 1
    if not reversible(n):
        return 0
    res = 1
    if digits % 2 == 1 and even[len(even) - 1]:
        return 0
    for i in range(digits // 2):
        if carry[i]:
            if even[i]:
                res *= 25
            else:
                res *= 20
        else:
            if even[i]:
                if i == 0:
                    res *= 20
                else:
                    res *= 25
            else:
                if i == 0:
                    res *= 20
                else:
                    res *= 30
    if digits % 2 == 1:
        res *= 5
    return res
