"""
https://leetcode.com/problems/non-overlapping-intervals
Using greedy algorithm
"""
#1. My Solution (1322ms)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def maximumNonOverlappingIntervals(intervals):
            intervals.sort(key=lambda x: x[1])

            count = 1
            x_end = intervals[0][1]

            for interval in intervals:
                if (interval[0] >= x_end):
                    count += 1
                    x_end = interval[1]


            return count

        return len(intervals) - maximumNonOverlappingIntervals(intervals)
