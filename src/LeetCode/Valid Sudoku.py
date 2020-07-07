"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
"""
#1. My Solution
from itertools import product


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        for i in range(9):
            temp_rows = set()
            temp_cols = set()
            for j in range(9):
                if board[i][j] in temp_rows or board[j][i] in temp_cols:
                    return False
                else:
                    if board[i][j] != '.':
                        temp_rows.add(board[i][j])
                    if board[j][i] != '.':
                        temp_cols.add(board[j][i])
        
        offset = [[0, 3, 6], [0, 3, 6]]
        for a, b in product(*offset):
            temp_square = set()
            for i in range(3):            
                for j in range(3):
                    if board[i+a][j+b] in temp_square:
                        return False
                    elif board[i+a][j+b] != '.':
                        temp_square.add(board[i+a][j+b])
                        
        return True
        
#2. Optimal Solution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for i in range(9)]
        row = [set() for i in range(9)]
        cell = [[set() for i in range(3)] for j in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                
                if board[i][j] in col[j]: return False
                else: col[j].add(board[i][j])
                    
                if board[i][j] in row[i]: return False
                else: row[i].add(board[i][j])
                    
                ci = i // 3
                cj = j // 3
                
                if board[i][j] in cell[ci][cj]: return False
                else: cell[ci][cj].add(board[i][j])
        
        return True
