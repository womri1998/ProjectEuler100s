def gen_primes(n):
    done = 0
    primes = []
    while n != 0:
        if n < 10 ** 6:
            suspects = [True] * n
            n = 0
        else:
            suspects = [True] * 10 ** 6
            n -= 10 ** 6
        if done == 0:
            suspects[0], suspects[1] = False, False
        for p in primes:
            r = 0 if done % p == 0 else p - done % p
            for i in range(r, len(suspects), p):
                suspects[i] = False
        for i in range(len(suspects)):
            if suspects[i]:
                for j in range(2 * i + done, len(suspects), i + done):
                    suspects[j] = False
        primes += [i + done for i in range(len(suspects)) if suspects[i]]
        done += 10 ** 6
        print(done)
    return primes


primes = gen_primes(10 ** 8)


def semiprimes(n):
    count = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] * primes[j] < n:
                #print(primes[i] * primes[j], primes[i], primes[j])
                count += 1
            else:
                break
    return count
