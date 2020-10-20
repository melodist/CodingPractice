"""
https://www.hackerrank.com/challenges/unbounded-knapsack/problem
Using dynamic programming
"""
#1. My Solution
def unboundedKnapsack(k, arr):
    ans = [0] * (k+1)

    arr = sorted([*set(arr)])
    n = len(arr)

    for a in arr:
        for j in range(1, k+1):
            if a <= j:
                ans[j] = max(ans[j], a + ans[j-a])
    
    return ans[-1]
