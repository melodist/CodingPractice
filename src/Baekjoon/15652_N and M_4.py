"""
https://www.acmicpc.net/problem/15652
"""
def generate(arr):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(arr[-1], n+1):
        generate(arr + [i])
    
n, m = map(int, input().split())
for i in range(n):
    generate([i+1])
