"""
https://www.hackerrank.com/challenges/a-chessboard-game-1/problem
Using observation
"""
#1. My Solution
def chessboardGame(x, y):
    x %= 4
    y %= 4
    return 'First' if x == 0 or x == 3 or y == 0 or y == 3 else 'Second'
