"""
https://www.hackerrank.com/challenges/sherlock-and-cost/problem
Using Memoization
Note that there are only 2 cases for choosing A[i] value.
1. Choosing 1
2. Choosing B[i]
"""
def cost(B):
    n = len(B)
    hi, low= 0, 0
    for i in range(1, n):
        high_to_low_diff = abs(B[i-1] - 1)
        low_to_high_diff = abs(B[i] - 1)
        high_to_high_diff = abs(B[i] - B[i-1])
        
        low_next = max(low, hi+high_to_low_diff)
        hi_next = max(hi+high_to_high_diff, low+low_to_high_diff)
        
        low = low_next
        hi = hi_next
    
    return max(hi,low)
