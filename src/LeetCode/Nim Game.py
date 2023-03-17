"""
https://leetcode.com/problems/nim-game
To win the game, you should always 1~3 stone
Opposite player will win if 4 stones left
So, n should not be 
"""
#1. My Solution (32ms)
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
