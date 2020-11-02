"""
https://www.acmicpc.net/problem/14719
Implementation problem
"""
#1. My Solution
h, w = map(int, input().split())
arr = [*map(int, input().split())]
answer = 0

for i, a in enumerate(arr[1:-1], 1):
    left = max(arr[:i])
    right = max(arr[i+1:])
    second = min(left, right)
    if a < second:
        answer += second - a

print(answer)

#2. Other Solution
H,W=map(int,input().split())
A=list(map(int,input().split()))
M=[]
m = -1
# Find right border
for i in range(len(A)-1,-1,-1):
	if m < A[i]: m = A[i]
	M = [m] + M

R = 0
m = A[0]
# Find left border and answer
for i in range(1, len(A)-1):
	t = min(m, M[i]) - A[i]
	if t > 0: R += t
	if m < A[i]: m = A[i]
print(R)
