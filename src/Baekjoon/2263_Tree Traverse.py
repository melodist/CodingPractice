"""
https://www.acmicpc.net/problem/2263
Using divide and conquer
"""
#1. My Solution
import sys


def divide(in_start, in_end, post_start, post_end):
    if post_start > post_end:
        return
    
    root = postorder[post_end]
    print(root, end=' ')
    
    # Left subtree
    divide(in_start, idx[root]-1, post_start, post_start + (idx[root] - in_start) - 1)
    # Right subtree
    divide(idx[root]+1, in_end, post_start + (idx[root] - in_start), post_end - 1)


sys.setrecursionlimit(10**6)
n = int(input())
inorder = [*map(int, input().split())]
postorder = [*map(int, input().split())]

idx = [0] * (n+1)
for i in range(n):
    idx[inorder[i]] = i

divide(0, n-1, 0, n-1)
