def max_sum(arr):
    best, max, min, cur = 0, 0, 0, 0
    for i in range(len(arr)):
        cur += arr[i]
        if cur > max:
            max = cur
            best = max - min
        elif cur < min:
            min = cur
    return best


def gen_mat():
    arr = [(100003 - 200003 * (k + 1) + 300007 * (k + 1) ** 3) % 10 ** 6 - 5 * 10 ** 5 for k in range(55)]
    for k in range(55, 4 * 10 ** 6):
        arr.append((arr[k - 24] + arr[k - 55]) % 10 ** 6 - 5 * 10 ** 5)
    arr2 = []
    for i in range(2000):
        arr2.append([])
        for j in range(2000):
            arr2[i].append(arr[i * 2000 + j])
    return arr2


def lines(mat):
    best = 0
    for l in mat:
        x = max_sum(l)
        if x > best:
            best = x
    return best


def columns(mat):
    cols = []
    for x in mat[0]:
        cols.append([])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            cols[j].append(mat[i][j])
    best = 0
    for c in cols:
        x = max_sum(c)
        if x > best:
            best = x
    return best


def diagonals(mat):
    dias = []
    for i in range(len(mat) + len(mat[0]) - 1):
        dias.append([])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i >= j:
                dias[i - j].append(mat[i][j])
            else:
                dias[len(mat) + j - i - 1].append(mat[i][j])
    best = 0
    for d in dias:
        x = max_sum(d)
        if x > best:
            best = x
    return best


def anti_diagonals(mat):
    anti = []
    for i in range(len(mat) + len(mat[0]) - 1):
        anti.append([])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
                anti[i + j].append(mat[i][j])
    best = 0
    for d in anti:
        x = max_sum(d)
        if x > best:
            best = x
    return best


def res():
    mat = gen_mat()
    return max([lines(mat), columns(mat), diagonals(mat), anti_diagonals(mat)])
