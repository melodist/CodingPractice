"""
https://leetcode.com/contest/weekly-contest-294/problems/maximum-bags-with-full-capacity-of-rocks/
Weekly Contest 294
Using greedy algorithm
"""
#1. My Solution (1285ms)
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        current_capacity = [c - r for c, r in zip(capacity, rocks)]
        current_capacity.sort()
        
        for i, c in enumerate(current_capacity):
            if additionalRocks >= c:
                additionalRocks -= c
                current_capacity[i] = 0
        
        return current_capacity.count(0)
