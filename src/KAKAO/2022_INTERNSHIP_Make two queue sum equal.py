"""
https://school.programmers.co.kr/learn/courses/30/lessons/118667
Concatnate two queues and find point that equals left and right
"""
#1. My Solution
from collections import deque


def solution(queue1, queue2):
    n = len(queue1)
    p1 = p2 = 0
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)

    q1 = deque(queue1)
    q2 = deque(queue2)

    while q1 and q2 and p1 + p2 < 3 * n:
        if sum_q1 > sum_q2:
            temp = q1.popleft()
            p1 += 1
            sum_q1 -= temp
            sum_q2 += temp
            q2.append(temp)
        elif sum_q1 < sum_q2:
            temp = q2.popleft()
            p2 += 1
            sum_q2 -= temp
            sum_q1 += temp
            q1.append(temp)
        else:
            return p1 + p2

    return -1
  
  #2. Other Solution
  def solution(que1, que2):
    queSum = (sum(que1) + sum(que2))
    if queSum % 2:
        return -1
    target = queSum // 2

    n = len(que1)
    start = 0
    end = n - 1
    ans = 0

    cur = sum(que1)
    que3 = que1 + que2
    while cur != target:
        if cur < target:
            end += 1
            if end == n * 2:
                return -1
            cur += que3[end]
        else:
            cur -= que3[start]
            start += 1
        ans += 1
    return ans
