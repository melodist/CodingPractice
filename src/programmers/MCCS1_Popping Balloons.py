"""
https://programmers.co.kr/learn/courses/30/lessons/68646/
We can pop a balloon which is smaller than left minimum or right minimum.
"""
def solution(a):
    answer = 2  # Left end and right end can be popped always
    n = len(a)
    min_left = a[0]
    mins_right = [0] * n
    mins_right[-2] = a[-1]
    for i, x in enumerate(a[-2::-1], 2):
        mins_right[n-i-1] = min(mins_right[n-i], x)

    for i, x in enumerate(a[1:-1], 1):
        if min_left > x or mins_right[i] > x:
            answer += 1
        min_left = min(x, min_left)
    return answer
