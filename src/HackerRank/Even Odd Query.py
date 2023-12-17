"""
https://www.hackerrank.com/challenges/even-odd-query
Mathematical Problem
1. If A[i] is odd, find(i, j) is always odd, including A[j] = 0
2. If A[i] is even, find(i, j) is always even except the case arr[i+1] = 0
2-1. If A[i] = 0, find(i, j) = 0 ** find(i+1, j) = 0
2-2. So, If A[i+1] = 0, find(i, j) = A[i] ** 0 = 1, will be odd
"""
#1. My Solution
def solve(arr, queries):
    result = []
    for i, j in queries:
        if arr[i-1]%2 == 1:
            result.append('Odd')
        elif i != j and arr[i] == 0:
            result.append('Odd')
        else:
            result.append('Even')
    return result
