"""
https://programmers.co.kr/learn/courses/30/lessons/43236
Using binary search
Change problem into find minimal distance x that removes stones less than n
"""
#1. My Solution
def solution(distance, rocks, n):
    rocks.sort()
    left = 1; right = distance
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        prev = 0
        for r in rocks:
            if r - prev < mid:
                cnt += 1
            else:
                prev = r
        
        # Check last rock
        if distance - prev < mid: cnt += 1
            
        if cnt <= n:
            ans = max(ans, mid)
            left = mid + 1
        else:
            right = mid - 1
            
    return ans
