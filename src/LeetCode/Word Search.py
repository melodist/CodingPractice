"""
https://leetcode.com/problems/word-search/
Solution using DFS
"""
#1. My Solution
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(ind, y, x):
            if ind == w - 1:
                return True
            
            for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if 0 <= x + dx < m and 0 <= y + dy < n:
                     if board[y+dy][x+dx] == word[ind+1] and not visited[y+dy][x+dx]:
                            visited[y+dy][x+dx] = True
                            if dfs(ind+1, y+dy, x+dx):
                                return True
                            else:
                                visited[y+dy][x+dx] = False
            return False
            
        n = len(board)
        m = len(board[0])
        w = len(word)
        for i in range(n):
            for j in range(m):
                if board[i][j] != word[0]: continue
                    
                visited = [[False] * m for _ in range(n)]
                visited[i][j] = True
                if dfs(0, i, j):
                    return True
            
        return False
