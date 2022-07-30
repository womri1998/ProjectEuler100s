def divisibility_number(n: int) -> int:
    length = 1
    last_residue = 1
    repunit = 1
    while repunit % n != 0:
        last_residue = (last_residue * 10) % n
        repunit = (repunit + last_residue) % n
        length += 1
    return length


def lowest_number(limit: int) -> int:
    residues = [1, 3, 7, 9]
    n = limit
    while True:
        if n % (limit // 100) == 0:
            print(n)
        for residue in residues:
            if divisibility_number(n + residue) >= limit:
                return n + residue
        n += 10


if __name__ == "__main__":
    print(lowest_number(10 ** 6))
