"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
"""
#1. My Solution
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i, x in enumerate(zip(*matrix)):
            matrix[i] = x[::-1]
        
#2. Other Solution
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()
