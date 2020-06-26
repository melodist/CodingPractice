"""
https://programmers.co.kr/learn/courses/30/lessons/64062
Find proper k value using Binary Search
Count continuous 0 in stepstones
"""
def solution(stones, k):
    left, right = 0, int(2E8)
    
    while left <= right:
        mid = (left + right) // 2
        
        if binary_search(stones, mid, k):
            right = mid - 1
        else:
            left = mid + 1

    return left

def binary_search(stones, n, k):
    count = 0
    for s in stones:
        if s - n <= 0:
            count += 1
        else:
            count = 0
            
        if count >= k:
            return True
            
    return False
