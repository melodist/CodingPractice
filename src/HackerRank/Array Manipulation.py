"""
https://www.hackerrank.com/challenges/crush/problem
"""
def arrayManipulation(n, queries):
    arr = [0] * (n+1)

    for a, b, k in queries:
        arr[a] += k
        if b < n:
            arr[b+1] -= k

    ans, x = 0, 0
    for i in range(1, n+1):
        x += arr[i]
        if x > ans:
            ans = x
            
    return ans
