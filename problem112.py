def bouncy(n):
    up, down = False, False
    while n >= 10:
        if n % 10 < (n // 10) % 10:
            down = True
        elif n % 10 > (n // 10) % 10:
            up = True
        n //= 10
    return up and down


def proportion(perc):
    i = 99
    count = 0
    while count / i < perc:
        i += 1
        if bouncy(i):
            count += 1
    return i
