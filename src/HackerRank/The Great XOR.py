"""
https://www.hackerrank.com/challenges/the-great-xor/problem
Using bit manipulations
"""
#1. My Solution
def theGreatXor(x):
    b = reversed(format(x, 'b'))
    ans = 0
    for i, a in enumerate(b):
        if a == '0':
            ans += 2 ** i
            
    return ans
