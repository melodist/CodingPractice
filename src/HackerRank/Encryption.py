"""
https://www.hackerrank.com/challenges/encryption/problem
"""
def encryption(s):
    L = len(s)
    L_root = math.sqrt(L)
    rows = math.floor(L_root)
    cols = math.ceil(L_root)

    if rows * cols < L: rows += 1

    arr = [0] * rows

    for i in range(rows-1):
        arr[i] = list(s[:cols])
        s = s[cols:]

    arr[-1] = list(s + " " * (cols - len(s)))

    arr = [''.join(list(x)) for x in zip(*arr)]
    arr = [s.rstrip() for s in arr]

    return ' '.join(arr)
