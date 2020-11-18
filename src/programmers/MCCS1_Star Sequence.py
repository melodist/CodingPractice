"""
https://programmers.co.kr/learn/courses/30/lessons/70130/
Using greedy algorithm
"""
#1. My Solution
from collections import defaultdict


def solution(a):
    inds = defaultdict(list)
    for i, x in enumerate(a):
        inds[x].append(i)

    answer, n = 0, len(a)

    nums = sorted(inds.keys(), key=lambda x:len(inds[x]), reverse=True)

    for k in nums:
        if len(inds[k]) < answer // 2:  # Need not to check number which has count less than maximum count in star sequence
            continue

        visited = [False] * n
        temp = 0

        for i in inds[k]:
            visited[i] = True
            if i > 0 and a[i-1] != k and not visited[i-1]:
                temp += 2
                visited[i-1] = True
            elif i + 1 < n and a[i+1] != k and not visited[i+1]:
                temp += 2
                visited[i+1] = True

        answer = max(temp, answer)

    return answer
