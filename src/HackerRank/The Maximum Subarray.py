"""
https://www.hackerrank.com/challenges/maxsubarray/problem
Using dynamic programming
"""
#1. My Solution
def maxSubarray(arr):
    ans1 = ans2 = t = arr[0]
    for a in arr[1:]:
        t = max(a, t + a)
        ans1 = max(ans1, t)
        if ans2 >= 0 and a > 0:
            ans2 += a
        elif ans2 < 0 and ans2 < a:
            ans2 = a

    return ans1, ans2

#2. Other Solution
def maxSubarray(arr):
    h = m = t = arr[0]
    for ind, n in enumerate(arr):
        if ind == 0: continue
        t = max(t, n, t + n)
        h = max(n, h + n)
        m = max(m, h)

    return m, t
