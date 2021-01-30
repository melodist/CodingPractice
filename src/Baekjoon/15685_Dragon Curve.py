"""
https://www.acmicpc.net/problem/15685
Using issubset() to check the curve has square points
"""
import sys

n = int(input())
points = set()

for i in range(n):
	
	x, y, d, g = map(int, sys.stdin.readline().split())
	xx = [1, 0, -1, 0]
	yy = [0, -1, 0, 1]
	# rotate 90 -> d += 1 / d % 4
	# (0) -> (0, 1) -> (0, 1, // 2, 1) -> (0, 1, 2, 1 // 2, 3, 2, 1)
	gg = [d]
	for i in range(g):
		rear = [(a+1) % 4 for a in gg[::-1]]
		gg += rear
	
	points.add((x, y))
	for comm in gg:
		x += xx[comm]
		y += yy[comm]
		points.add((x, y))

ans = 0
for i in range(100):
	for j in range(100):
		square = set([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])
		if square.issubset(points):
			ans += 1
			
print(ans)
