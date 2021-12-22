"""
https://leetcode.com/contest/weekly-contest-268/problems/two-furthest-houses-with-different-colors/
Implementation Problem
"""
#1. My Solution (52ms)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        answer = 0
        for i in range(n):
            for j in range(i+1, n):
                if colors[i] != colors[j]:
                    answer = max(answer, j-i)
                    
        return answer
