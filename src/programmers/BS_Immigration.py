"""
https://programmers.co.kr/learn/courses/30/lessons/43238/
Using Binary Search
Search minimal value that meets the condition.
"""
def solution(n, times):
    times.sort()
    left, right = 0, int(1E20)

    while left <= right:
        mid = (left + right) // 2

        if binary_search(times, mid, n):
            right = mid - 1
        else:
            left = mid + 1

    return left

def binary_search(times, ans, n):
    count = 0
    # Check if the immigration can ends with given time
    for t in times:
        count += ans // t  # Calculate people numbers by one officer

        if count >= n:
            return True

    return False
