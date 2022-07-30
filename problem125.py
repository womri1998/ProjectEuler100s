def sums_of_squares(n):
    i = 2
    res = []
    while i ** 2 + (i - 1) ** 2 < n:
        s = i ** 2 + (i - 1) ** 2
        j = i
        while s < n:
            insert(res, s)
            j += 1
            s += j ** 2
        i += 1
    return res


def insert(arr, n):
    l, h = 0, len(arr)
    while l < h:
        m = (l + h) // 2
        if arr[m] < n:
            l = m + 1
        elif arr[m] > n:
            h = m
        else:
            return
    return arr.insert(h, n)


def palindrome(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
