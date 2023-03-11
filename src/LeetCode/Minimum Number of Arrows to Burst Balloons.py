"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
Using greedy algorithm
Same as finding non-overlapping intervals
"""
#1. My Solution (1338ms)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])

        x_end = points[0][1]
        ans = 1

        for p in points:
            if x_end < p[0]:
                x_end = p[1]
                ans += 1

        return ans
