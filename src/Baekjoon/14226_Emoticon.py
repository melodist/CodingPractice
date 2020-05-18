"""
https://www.acmicpc.net/problem/14226
Using BFS. Don't forget to make visited.
"""
from collections import deque

s = int(input())
q = deque([(1, 0)])
visited = [[-1] * 1001 for _ in range(1001)]
visited[1][0] = 0

while q:
    cur, clip = q.popleft()
    if cur == s: 
        print(visited[cur][clip])
        break
    
    #1. Paste from clipboard
    if cur + clip < 1001:
        if visited[cur+clip][clip] == -1:
            q.append((cur+clip, clip))
            visited[cur+clip][clip] = visited[cur][clip] + 1
            
    #2. Copy current emoticons
    if visited[cur][cur] == -1:
        q.append((cur, cur))
        visited[cur][cur] = visited[cur][clip] + 1
    
    #3. Delete one emoticon
    if cur - 1 >= 0:
        if visited[cur-1][clip] == -1:
            q.append((cur-1, clip))
            visited[cur-1][clip] = visited[cur][clip] + 1
