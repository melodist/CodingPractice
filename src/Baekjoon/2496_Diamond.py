"""
https://www.acmicpc.net/problem/2496
Using sliding window and axis transform
x, y -> x+y, x-y
"""
#1. My Solution
def check(x, y):
    ret = 0
    for i, j in arr:
        if x <= i <= x+k and y <= j <= y+k:
            ret += 1
            
    return ret

n, m, t, k = map(int, input().split())
arr = [[] for _ in range(t)]

for i in range(t):
    x, y = map(int, input().split())
    arr[i] = [x+y, x-y]

ans, ans_x, ans_y = 0, 0, 0

for i in range(t):
    for j in range(t):
        x= arr[i][0]; y = arr[j][1]
        if (x+y) % 2:
            d = [(1, 0), (-1, 0), (0, 1), (0, -1), (-k//2, -k//2)]
        else:
            d = [(0, 0), (-k//2, -k//2)]
        for dx, dy in d:
            temp = check(x+dx, y+dy)
            a = (x+dx+y+dy) // 2
            b = (x+dx-y-dy) // 2
            if temp > ans and 0 <= a+k//2 <= n and 0 <= b <= m:
                ans = temp
                ans_x = a+k//2
                ans_y = b
           

print(ans_x, ans_y)
print(ans)
