"""
https://www.hackerrank.com/challenges/lexicographic-steps
Combinatorics Problem
"""
#1. My Solution
def solve(x, y, k):
    ans = ""
    while k > 0:
        if k < math.comb(x+y-1, y):
            ans += "H"
            x -= 1
        else:
            ans += "V"
            k -= math.comb(x+y-1, y)
            y -= 1
            
    ans += x * "H"
    ans += y * "V"
            
    return ans
