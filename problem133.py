def is_prime(number: int, primes: list[int]) -> bool:
    for prime in primes:
        if prime > number ** 0.5:
            break
        elif number % prime == 0:
            return False
    return True


def generate_primes(limit: int):
    primes = [2]
    for number in range(3, limit, 2):
        if is_prime(number, primes):
            primes.append(number)
    return primes


if __name__ == "__main__":
    n = 0
    for i in range(10):
        n += 10 ** (10 * i)
    print(n % (10 ** 10 + 1))
    print(n % (10 ** 50 + 1))
    print(n)
    print(n // (10 ** 10 + 1))
