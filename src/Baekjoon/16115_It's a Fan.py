"""
https://www.acmicpc.net/problem/16115
Geometric Problem
1. Find angle for points which has farthest distance from origin.
2. Find largest angle difference for neighbored points.
Note that input() is slow. Using sys.stdin.readline().strip() instead.
"""
import sys
import math


t = int(input())
arr = [sys.stdin.readline().strip() for i in range(t)]
points = []
r = 0

for s in arr:
    x, y = map(int, s.split())
    l = x**2 + y**2
    if l == r:
        points.append((x, y))
    elif l > r:
        r = l
        points.clear()
        points.append((x, y))
        
angles = [0] * len(points)
r **= 0.5

for i, (x, y) in enumerate(points):
    a = x / r
    angle = math.degrees(math.acos(a))
    if y < 0:
        angle = 360 - angle
    angles[i] = angle
    
angles.sort()
diff = [y - x if x < y else y - x + 360 for x, y in zip(angles, angles[1:] + [angles[0]])]
print(max(diff))
