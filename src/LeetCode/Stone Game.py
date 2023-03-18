"""
https://leetcode.com/problems/stone-game
1. All piles can be divided into odd and even index
2. All odd indexed piles or all even indexed piles has more stone than each other
3. First player can always take larger one, so first player always win
"""
#1. My Solution (37ms)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
