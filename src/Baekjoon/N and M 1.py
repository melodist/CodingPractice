"""
https://www.acmicpc.net/problem/15649
N, M이 작으므로 brute force로 해결
"""
def generate(chosen, used):
    if len(chosen) == m:
        print(' '.join(map(str, chosen)))
        return
        
    for i in range(n):
        if not used[i]:
            chosen.append(i+1)
            used[i] = 1
            generate(chosen, used)
            used[i] = 0
            chosen.pop()
            
n, m = map(int, input().split())
used = [0 for _ in range(n)]

generate([], used)
