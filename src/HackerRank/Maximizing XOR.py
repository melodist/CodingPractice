"""
https://www.hackerrank.com/challenges/maximizing-xor/problem
Implementation problem
"""
#1. Solution using brute force (O(n^2))
from itertools import combinations_with_replacement


def maximizingXor(l, r):
    ans = 0
    for a, b in combinations_with_replacement(range(l, r+1), 2):
        ans = max(ans, a ^ b)
        
    return ans

#2. Solution using the most significant bit
# l = 01000
# r = 11010
#     0xxxx
#      ↑ the most significant bit
def maximizingXor(l, r):
    return 2 ** (int(math.log2(l ^ r)) + 1) - 1
