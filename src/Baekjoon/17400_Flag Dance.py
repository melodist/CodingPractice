"""
https://www.acmicpc.net/problem/17400
Using Segment Tree
It can also be solved by using two segment tree holding odds and evens
"""
#1. Solution using Segment Tree
import sys
import math


# Segment Tree
# 1-Based approach would be convinient
# tree[1] - root, store sum of all values
# tree[node*2] start~mid
# tree[node*2+1] mid+1~end
class SegmentTree():
    def __init__(self, arr):
        self.arr = arr
        self.height = math.ceil(math.log2(n) + 1)
        self.length = len(arr)
        self.tree = [0] * (2 ** self.height)
        
    def initialize(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            value_l = self.initialize(node*2, start, mid)
            value_r = self.initialize(node*2+1, mid+1, end)
            if (end - mid) % 2 == 0:
                self.tree[node] = value_r + value_l
            else:
                self.tree[node] = value_r - value_l

        return self.tree[node]
        
    def find(self, left, right, node, start, end):
        # left, right : Interval to find
        # start, end : start and end of node
        if left > end or right < start:
            return 0
        # Interval to find includes interval of node
        elif left <= start and right >= end:
            return self.tree[node] if (end - right) % 2 == 0 else -self.tree[node]
        else:
            mid = (start + end) // 2
            value_l = self.find(left, right, node*2, start, mid)
            value_r = self.find(left, right, node*2+1, mid+1, end)
            return value_r + value_l
            
    def update(self, target, value, node, start, end):
        if start <= target <= end:
            # Add the value if the target is added
            if (end - target) % 2 == 0:
                self.tree[node] += value
            # Subtract the value if the target is subtracted
            else:
                self.tree[node] -= value
            if start != end:
                mid = (start + end) // 2
                self.update(target, value, node*2, start, mid)
                self.update(target, value, node*2+1, mid+1, end)
                
        
n, q = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
t = SegmentTree(arr)
t.initialize(1, 0, t.length-1)

for _ in range(q):
    comm, l, r = map(int, sys.stdin.readline().strip().split())
    if comm == 1:
        print(abs(t.find(l, r, 1, 1, t.length)))
    else:
        t.update(l, r, 1, 1, t.length)

#2. Solution using Brute Force
import sys


n, q = map(int, input().split())
C = [0] + list(map(int, sys.stdin.readline().strip().split()))

for i, x in enumerate(C[1:], 1):
    C[i] = C[i] - C[i-1]

for _ in range(q):
    comm, l, r = map(int, sys.stdin.readline().strip().split())
    if comm == 1:
        if (r - l) % 2 == 0:
            print(abs(C[r] + C[l-1]))
        else:
            print(abs(C[r] - C[l-1]))
    else:
        for i in range(l, len(C), 2):
            C[i] += r
            
        for i in range(l+1, len(C), 2):
            C[i] -= r
            
