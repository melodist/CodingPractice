"""
https://www.hackerrank.com/challenges/even-odd-query
Mathematical Problem
"""
#1. My Solution
def solve(arr, queries):
    result = []
    for i, j in queries:
        if arr[i-1]%2 == 0:
            result.append('Odd')
        elif i != j and arr[i] == 0:
            result.append('Odd')
        else:
            result.append('Even')
    return result
