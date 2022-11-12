"""
https://leetcode.com/problems/n-queens
Using Backtracking
"""
#1. My Solution (363ms)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(board, row):
            if (row == len(board)):
                res.append([''.join(board[i]) for i in range(n)])
                return True
            
            for col in range(len(board)):
                if not isValid(board, row, col):
                    continue
                board[row][col] = "Q"
                backtrack(board, row+1)
                board[row][col] = "."

        def isValid(board, row, col):
            n = len(board)
            # Find queen in same column
            for i in range(row):
                if board[i][col] =='Q':
                    return False
                
            # Find queen in left upper
            for i in range(min(row, col)):
                  if board[row-i-1][col-i-1] =='Q':
                    return False

            # Find queen in right upper
            for i in range(min(row, n-col-1)):
                  if board[row-i-1][col+i+1] =='Q':
                    return False

            return True

        board = [['.' for i in range(n)] for i in range(n)]
        res = []
        backtrack(board, 0)
        return res
    
    
#2. Other Solution (52ms)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        state = [['.' for _ in range(n)] for _ in range(n)]
        def append_answer(state):
            board = []
            for row in state:
                board.append(''.join(row))
            ans.append(board)
        
        def backtrack(row, diagonals, anti_diagonals, cols, state):
            if row == n:
                append_answer(state)
            
            for col in range(n):
                diag = row-col
                anti_diag = row+col
                
                if (col in cols or
                    diag in diagonals or
                    anti_diag in anti_diagonals):
                    continue
                
                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)
                state[row][col] = 'Q'

                backtrack(row+1, diagonals, anti_diagonals, cols, state)

                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)
                state[row][col] = '.'
        
        backtrack(0, set(), set(), set(), state)
        return ans
