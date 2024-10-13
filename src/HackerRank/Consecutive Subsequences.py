"""
https://www.hackerrank.com/challenges/consecutive-subsequences
Combinatorics Problem
"""
#1. My Solution
from itertools import accumulate

t = int(input())
while t:
    s, t = 0, t-1
    n, k = map(int, input().split())  
    prefix = accumulate(map(int, input().split())) # prefix sum oneliner
    rem = [i%k for i in prefix]
    count = [1] + [0] * (k-1)
    for i in rem:   count[i] += 1
    for i in count: s += (i*(i-1))//2
    print(s)
