"""
https://www.acmicpc.net/problem/16946
Using memoization and BFS.
Labeling the region with zero values.
"""
from collections import deque
import sys

class BFS():
    
    def __init__(self, arr):
        self.memo = {}
        self.label = 1
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.arr = arr
        self.zeros = [[0] * m for _ in range(n)]
    
    def bfs1(self, start):
        visited = set([start])
        q = deque([start])
    
        while q:
            x, y = q.popleft()

            if self.arr[y][x] == '1':
                self.arr[y][x] = self.bfs2((x, y))
                self.zeros[y][x] = -1
            else:
                if self.zeros[y][x] == 0:
                    self.memo[self.label] = self.bfs_labeling((x, y))
                    self.label += 1
            
            for dx, dy in self.directions:
                if 0 <= x+dx < m and 0 <= y+dy < n \
                    and (x+dx, y+dy) not in visited:
                    q.append((x+dx, y+dy))
                    visited.add((x+dx, y+dy))
    
    def bfs2(self, start):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        x, y = start
        temp = set()
        
        for dx, dy in self.directions:
            if 0 <= x+dx < m and 0 <= y+dy < n:
                if self.zeros[y+dy][x+dx] > 0:
                    temp.add(self.zeros[y+dy][x+dx])
                elif self.arr[y+dy][x+dx] == '0':
                    self.memo[self.label] = self.bfs_labeling((x+dx, y+dy))
                    temp.add(self.label)
                    self.label += 1
                    
        ans = 0
        for l in temp:
            ans += self.memo[l]
            
        return (ans + 1) % 10
        
    def bfs_labeling(self, start):
        
        visited = set([start])
        q = deque([start])
        count = 0
    
        while q:
            x, y = q.popleft()
            
            for dx, dy in self.directions:
                if 0 <= x+dx < m and 0 <= y+dy < n \
                    and (x+dx, y+dy) not in visited \
                    and self.arr[y+dy][x+dx] == '0':
                        q.append((x+dx, y+dy))
                        visited.add((x+dx, y+dy))
                    
            count += 1
            self.zeros[y][x] = self.label
            
        return count
    
    
n, m = map(int, sys.stdin.readline().split())
arr = [[0] * m for _ in range(n)]

for i in range(n):
    row = list(sys.stdin.readline().rstrip())
    arr[i] = row
    
ans = BFS(arr)
ans.bfs1((0, 0))

[print(''.join(map(str, ans.arr[i]))) for i in range(n)]
