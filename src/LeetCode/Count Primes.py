"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
"""
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1: return 0
        visited = [0] * n
        for i in range(2, int(math.sqrt(n-1))+1):
            if visited[i] == 1:
                continue
            j = i * 2
            while j < n:
                visited[j] = 1
                j += i
            
        return visited.count(0) - 2
