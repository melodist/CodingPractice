"""
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
Implementation Problem
Make Complement Bucket
"""
#1. My Solution - O(n)
def divisibleSumPairs(n, k, ar):
    complements = [0] * k
    answer = 0

    for i in ar:
        answer += complements[k - (i % k)] if i % k != 0 else complements[0]
        complements[i % k] += 1
        
    return answer
    
#2. Other Solution - O(n^2)
# Using True = 1
def divisibleSumPairs(n, k, ar):
    return sum((i+j)%k == 0 for x, i in enumerate(ar) for j in ar[x+1:])
