"""
https://www.hackerrank.com/challenges/common-child/problem
Longest Common Sequence (LCS) Problem
"""
#1. My Solution
def commonChild(s1, s2):
    n, m = len(s1), len(s2)
    lcs = [[0] * (m + 1) for _ in range(n + 1)]

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

    return lcs[n - 1][m - 1]
    
#2. Other Solution
def commonChild(s1, s2):
    prev = [0] * (len(s2)+1)
    curr = [0] * (len(s2)+1)

    for r in s1:
        for j, c in enumerate(s2, 1):
            curr[j] = prev[j-1] + 1 if r == c else max(prev[j], curr[j-1])
        prev, curr = curr, prev

    return prev[-1]
