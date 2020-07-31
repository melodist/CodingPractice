"""
https://www.hackerrank.com/challenges/sherlock-and-array/problem
"""
#1. My Solution
def balancedSums(arr):
    total = sum(arr)
    left = 0
    for i in arr:
        if left == total - (i + left):
            return 'YES'
        left += i

    return 'NO'
