"""
https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
"""
def countSwaps(a):
    c = 0
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                c += 1

    print(f'Array is sorted in {c} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
