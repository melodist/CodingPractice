"""
https://www.acmicpc.net/problem/12851
Using BFS
"""
#1. My Solution
import sys
from collections import deque


def solve(n, k):
    if n >= k:
        return n - k, 1
        
    q = deque([n])
    MAX = 100000
    counts = [0] * (MAX+1)
    times = [sys.maxsize] * (MAX+1)
    times[n] = 0
    counts[n] = 1

    while q:
        u= q.popleft()
        if u+1 <= MAX and times[u+1] >= times[u] + 1:
            if times[u+1] == times[u] + 1:
                counts[u+1] = counts[u+1] + counts[u]
            else:
                times[u+1] = times[u] + 1
                counts[u+1] = counts[u+1] + counts[u]
                q.append(u+1)
        
        if u-1 >= 0 and times[u-1] >= times[u] + 1:
            if times[u-1] == times[u] + 1:
                counts[u-1] = counts[u-1] + counts[u]
            else:
                times[u-1] = times[u] + 1
                counts[u-1] = counts[u-1] + counts[u]
                q.append(u-1)
                
        if 2*u <= MAX and times[2*u] >= times[u] + 1:
            if times[2*u] == times[u] + 1:
                counts[2*u] = counts[2*u] + counts[u]
            else:
                times[2*u] = times[u] + 1
                counts[2*u] = counts[2*u] + counts[u]
                q.append(2*u)
                
    return times[k], counts[k]

time, count = solve(*map(int, input().split()))
print(time)
print(count)

#2. Other Solution
from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N-K)
    print(1)

else:
    visited = [False] * 100001
    ans = 100001
    amount = 0
    q = deque()
    q.append((K, 0))
    while q:
        pos, cnt = q.popleft()
        visited[pos] = True

        if cnt > ans:
            continue

        if pos == N:
            if cnt < ans:
                ans = cnt
                amount = 1
            elif cnt == ans:
                amount += 1
        
        else:
            if not pos % 2 and not visited[pos % 2]:
                q.append((pos // 2, cnt + 1))
            if 0 <= pos - 1 and not visited[pos-1]:
                q.append((pos - 1, cnt + 1))
            if pos + 1 <= 100000 and not visited[pos+1]:
                q.append((pos + 1, cnt + 1))

    print(ans)
    print(amount)
