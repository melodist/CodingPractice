"""
https://programmers.co.kr/learn/courses/30/lessons/43237
"""
def solution(budgets, M):
    if sum(budgets) < M:
        return max(budgets)

    left, right, temp = 0, max(budgets), 0

    while left <= right:
        mid = (left + right) // 2

        if temp == mid:
            return mid

        b = [a if a < mid else mid for a in budgets]

        if M > sum(b):
            left = mid
        else:
            right = mid

        temp = mid
