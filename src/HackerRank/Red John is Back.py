"""
https://www.hackerrank.com/challenges/red-john-is-back/problem
Using combinatorics
"""
#1. My Solution
def redJohn(n):
    if n < 4:
        return 0
    elif n == 4:
        return 1

    x = 1
    for i in range(n // 4):
        x += (math.factorial(n - 3 * (i+1)) / (math.factorial(n - 4 * (i+1)) * math.factorial(i+1)))

    x = int(x)
    visited = [False] * (x+1)
    ans = 0
    print(x)
    for i in range(2, x+1):
        if visited[i]:
            continue
        ans += 1
        for j in range(i * 2, x+1, i):
            visited[j] = True

    return ans
