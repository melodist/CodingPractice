"""
https://leetcode.com/problems/dungeon-game/
Implementation Problem
"""
#1. Solution using DP(Dynamic Programming) and binary search
class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def isGood(initHealth):
            dp = [[0] * n for _ in range(m)]
            dp[0][0] = initHealth + grid[0][0]
            for r in range(m):
                for c in range(n):
                    if r > 0 and dp[r-1][c] > 0:
                        dp[r][c] = max(dp[r][c], dp[r-1][c] + grid[r][c])
                    if c > 0 and dp[r][c-1] > 0:
                        dp[r][c] = max(dp[r][c], dp[r][c-1] + grid[r][c])
            return dp[m-1][n-1] > 0
        
        left = 1
        right = 1000 * (m + n) + 1
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if isGood(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

#2. Solution using DFS
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        self.end = (len(dungeon) - 1, len(dungeon[0]) - 1)
        if self.end == (0, 0) and dungeon[0][0] > 0: return 1
        if self.end == (0, 0): return -dungeon[0][0] + 1
        most_neg = self.rdfs((0 ,0), dungeon, {})
        if most_neg > 0: return 1
        return -most_neg + 1
    
    def rdfs(self, pos, matrix, memo):
        right = (pos[0], pos[1] + 1)
        down = (pos[0] + 1, pos[1])
        min_r, min_d = -float('inf'), -float('inf')
        if right[1] < len(matrix[0]):
            min_r = self.recurse(right, matrix, memo)
        if down[0] < len(matrix):
            min_d = self.recurse(down, matrix, memo)
			
        if (min_r < 0 and min_d < 0) or matrix[pos[0]][pos[1]] >= 0:
            memo[pos] =  max(min_r, min_d) + matrix[pos[0]][pos[1]]
        else: 
            memo[pos] = matrix[pos[0]][pos[1]]
        return memo[pos]
        
    def recurse(self, pos, matrix, memo):
        if pos in memo: return memo[pos]
        if pos == self.end: return matrix[pos[0]][pos[1]]
        return self.rdfs(pos, matrix, memo)
