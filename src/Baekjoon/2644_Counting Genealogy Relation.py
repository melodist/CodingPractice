"""
https://www.acmicpc.net/problem/2644
Using BFS
"""
#1. My Solution (96ms)
from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
tree = [[] for _ in range(n+1)]
parents = [0] * (n+1)
top = [True] * (n+1)
depth = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    tree[u].append(v)
    parents[v] = u
    top[v] = False

for i in range(1, n+1):
    if top[i]:
        q = deque([i])
        
        while q:
            u = q.popleft()
            for v in tree[u]:
                depth[v] = depth[u] + 1
                q.append(v)

if depth[a] < depth[b]:
    a, b = b, a # depth[a] >= depth[b]

ans = depth[a] - depth[b]    
for _ in range(ans):
    a = parents[a]
    
while a != b:
    a = parents[a]
    b = parents[b]
    ans += 2
    
print(ans if a > 0 else -1)

#2. Other Solution (56ms)
people = [[0]*101 for i in range(101)]
v = [0]*101

n = int(input(""))
p1, p2 = input("").split(" ")
m = int(input(""))

for i in range(m):
  x, y = input("").split(" ")
  x = int(x)
  y = int(y)
  people[x][y] = people[y][x] = 1
  
q = []
q.append(int(p1))

while q!=[] :
  present = q.pop(0)
  for i in range(1,n+1):
    if people[present][i] != 0 and v[i] == 0:
      v[i] = v[present]+1
      q.append(i)

if(v[int(p2)]!=0):
  print(v[int(p2)])
else:
  print(-1)
