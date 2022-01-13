"""
https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
Using greedy approach
"""
#1. My Solution (616ms)
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        piles = piles[:len(piles) * 2 // 3]
        return sum([x for i, x in enumerate(piles) if i % 2 == 1])
    
#2. Other Solution (564ms)
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        # print(piles)
        return sum(piles[1:2*len(piles)//3:2])
