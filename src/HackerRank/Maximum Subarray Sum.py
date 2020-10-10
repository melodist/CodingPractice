"""
https://www.hackerrank.com/challenges/maximum-subarray-sum/problem
Using binary search
"""
#1. My Solution
import bisect


def maximumSum(a, m):
    n = len(a)
    ans = 0 
    found = [] 
    a[0]= a[0] % m 
    for i in range(1, n): 
        a[i] = (a[i - 1] + a[i])%m 

    for i in range(n): 
        x = a[i] 
        j = bisect.bisect_right(found, x) 
        ans = max(ans, x) 
        if j < i: #sub array from j+1, i may be a solution 
            ans = max(ans, (a[i] - found[j]) % m) 
        found.insert(j, x)

    return ans
