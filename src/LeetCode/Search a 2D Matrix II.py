"""
https://leetcode.com/problems/search-a-2d-matrix-ii/
Search Problem
"""
#1. My Solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            for val in row:
                if val == target: return True
                
        return False
    
#2. Other Solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외처리
        if not matrix:
            return False
        
        # 첫 행의 맨뒤를 기준으로 판단
        row = 0
        col = len(matrix[0]) - 1
        
        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        
        return False
