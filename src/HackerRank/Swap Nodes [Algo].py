"""
https://www.hackerrank.com/challenges/swap-nodes-algo/problem
"""
#1. My Solution
from collections import defaultdict


def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    n = len(indexes)
    left = {}
    right = {}
    depth = {1:1}
    answer = []

    for i, (l, r) in enumerate(indexes):
        left[i+1] = l
        right[i+1] = r
        depth[l] = depth[i+1] + 1
        depth[r] = depth[i+1] + 1

    for k in queries:
        for q in range(k, n+1, k):
            for i in range(1, n+1):
                if depth[i] == q:
                    left[i], right[i] = right[i], left[i]

        stack = []
        temp = []
        cur = 1

        while stack or cur != -1:
            while cur != -1:
                stack.append(cur)
                cur = left[cur]

            cur = stack.pop()
            temp.append(cur)
            cur = right[cur]

        answer.append(temp)
            
    return answer
