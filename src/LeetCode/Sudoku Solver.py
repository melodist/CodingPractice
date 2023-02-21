"""
https://leetcode.com/problems/sudoku-solver
Using backtracking
"""
#1. My Solution (766ms)
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(board, i, j):
            if j == 9:
                return backtrack(board, i+1, 0)

            if i == 9:
                return True

            if board[i][j] != '.':
                return backtrack(board, i, j+1)

            for n in range(9):
                if not is_valid(board, i, j, str(n+1)):
                    continue
                
                board[i][j] = str(n+1)
                if backtrack(board, i, j+1):
                    return True
                board[i][j] = '.'

            return False

        def is_valid(board, r, c, n):
            for i in range(9):
                if board[r][i] == n:
                    return False

                if board[i][c] == n:
                    return False
                    
                if board[int(r/3)*3 + int(i/3)][int(c/3)*3 + i%3] == n:
                    return False

            return True

        backtrack(board, 0, 0)
        
#2. Other Solution (51ms)
from collections import defaultdict
from itertools import product

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """heuristic"""
        row, col, box = defaultdict(set), defaultdict(set), defaultdict(set)
        blank, alphabet = defaultdict(set), "123456789"

        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c is '.':
                    blank[(i, j)]
                else:
                    row[i].add(c)
                    col[j].add(c)
                    box[(i // 3, j // 3)].add(c)

        for i, j in blank:
            for c in alphabet:
                if c not in row[i] and c not in col[j] and c not in box[(i // 3, j // 3)]:
                    blank[(i, j)].add(c)


        def fill(i, j, k, c):
            is_legal, modified = True, []
            for other, valids in blank.items():
                if c in valids:
                    x, y = other
                    z = x // 3, y // 3
                    if x == i or y == j or z == k:
                        valids.remove(c)
                        modified.append(other)
                        if not valids:
                            is_legal = False
                            break
            return is_legal, modified


        def dfs():
            if not blank:
                return True
            pos = min(blank, key=lambda x: len(blank[x]))
            i, j = pos
            k = i // 3, j // 3
            cands = blank.pop(pos)
            for c in cands:
                is_legal, modified = fill(i, j, k, c)
                if is_legal:
                    board[i][j] = c
                    if dfs():
                        return True
                for other in modified:
                    blank[other].add(c)
                board[i][j] = '.'

            blank[pos] = cands
            return False

        dfs()
            
