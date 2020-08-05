"""
https://www.hackerrank.com/challenges/pairs/problem
"""
#1. My Solution
def pairs(k, arr):
    arr = set(arr)
    visited = set()
    answer = 0
    
    for a in arr:
        if a - k in arr and a - k not in visited:
            answer += 1
            visited.add(k-a)

    return answer
    
#2. Optimal Solution
def pairs(k, arr):
    a = set(arr)
    b = set([a - k for a in arr])
    
    return len(a & b)
