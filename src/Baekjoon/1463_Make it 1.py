"""
https://www.acmicpc.net/problem/1463
Using BFS
"""
#1. My Solution (116ms)
from collections import deque


n = int(input())
cnt = [-1] * (n+1)
cnt[n] = 0
q = deque([n])

while n != 1:
    u = q.popleft()
    if u == 1:
        break
    
    if u % 3 == 0 and cnt[u // 3] == -1:
        cnt[u // 3] = cnt[u] + 1
        q.append(u // 3)
    if u % 2 == 0 and cnt[u // 2] == -1:
        cnt[u // 2] = cnt[u] + 1
        q.append(u // 2)
    if cnt[u - 1] == -1:
        cnt[u - 1] = cnt[u] + 1
        q.append(u-1)
    
print(cnt[1])

#2. Other Solution (56ms)
save = {1:0, 2:1}
def frog(n):
    if n in save:
        return save[n]
    m = 1+min(frog(n//2)+n%2, frog(n//3)+n%3)
    save[n] = m
    return m

n = int(input())
print(frog(n))
