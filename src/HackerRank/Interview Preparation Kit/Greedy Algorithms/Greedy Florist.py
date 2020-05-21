"""
https://www.hackerrank.com/challenges/greedy-florist/problem
"""
def getMinimumCost(k, c):
    n = len(c)
    c.sort()
    ans = 0
    for i in range(n):
        ans += c[n-1-i] * (i // k + 1)

    return ans
