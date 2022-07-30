def gen_next(arr):
    if len(arr) != 55:
        k = len(arr) + 1
        arr.append((100003 - 200003 * k + 300007 * k ** 3) % 10 ** 6)
    else:
        arr.append((arr[0] + arr[31]) % 10 ** 6)
        arr = arr[1:]
    return arr


def next_call(arr, friends, representative):
    arr = gen_next(gen_next(arr))
    miss = (arr[-2] == arr[-1])
    x, y = representative[arr[-2]], representative[arr[-1]]
    if x != y:
        if len(friends[y]) > len(friends[x]):
            x, y = y, x
        for z in friends[y]:
            representative[z] = x
        friends[x] += friends[y]
        friends.pop(y)
        print("friends: " + str(len(friends)))
    return arr, friends, representative, miss


def first():
    count = 0
    arr = []
    friends = {i: [i] for i in range(10 ** 6)}
    representative = [i for i in range(10 ** 6)]
    while len(friends[representative[524287]]) < 990000:
        arr, friends, representative, miss = next_call(arr, friends, representative)
        if not miss:
            count += 1
        if count % 10 ** 3 == 0:
            print("count: " + str(count))
    return count
