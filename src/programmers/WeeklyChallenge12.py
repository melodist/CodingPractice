"""
https://programmers.co.kr/learn/courses/30/lessons/87946
Using backtracking
"""
#1. My Solution
class Solver:
    def __init__(self, dungeons):
        self.dungeons = dungeons
        self.answer = 0
        self.n = len(dungeons)
        self.visited = [False] * self.n
    
    def backtrack(self, f, i, rooms):
        for j in range(self.n):
            if i == j: 
                continue
            if f >= self.dungeons[j][0] and not self.visited[j]:
                self.visited[j] = True
                self.backtrack(f - self.dungeons[j][1], j, rooms + 1)
                self.visited[j] = False
                
            self.answer = max(self.answer, rooms)
    
def solution(k, dungeons):
    solve = Solver(dungeons) 
    solve.backtrack(k, -1, 0)
    return solve.answer

#2. Other Solution
solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])
