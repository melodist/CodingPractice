"""
https://www.acmicpc.net/problem/15650
"""
def generate(chosen):
    if len(chosen) == m:
        print(' '.join(map(str, chosen)))
        return
    
    for i in range(chosen[-1] + 1, n + 1):
        chosen.append(i)
        generate(chosen)
        chosen.pop()
    
    
n, m = map(int, input().split())
used = [0] * n
for i in range(n):
    generate([i+1])
