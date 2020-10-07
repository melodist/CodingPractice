"""
https://www.acmicpc.net/problem/12852
Using BFS
"""
#1. My Solution
from collections import deque


x = int(input())
visited = [0] * (x+1)
q = deque([(x, [x])])
while q:
    cur, path = q.popleft()
    if cur == 1:
        print(visited[1])
        print(' '.join(map(str, path)))
        break
    
    for i in (2, 3):
        a, r = divmod(cur, i)
        if r == 0 and visited[a] == 0:
            q.append((a, path + [a]))
            visited[a] = visited[cur] + 1
            
    if visited[cur - 1] == 0:
        q.append((cur - 1, path + [cur - 1]))
        visited[cur - 1] = visited[cur] + 1

#2. Other Solution
save = {1:0, 2:1}
def frog(n):
    if n in save.keys():
        return save[n]
    m = min(frog(n//2)+1+n%2, frog(n//3)+1+n%3)
    save[n] = m
    return m

n = int(input())
print(frog(n))
m = n
ans = [n]
while m > 1:
    if save[m] == save[m // 2] + 1 + m%2:
        if m%2:
            m -= 1
            ans.append(m)
        m //= 2
        ans.append(m)
    else:
        while m % 3:
            m -= 1
            ans.append(m)
        m //= 3
        ans.append(m)
print(*ans)
