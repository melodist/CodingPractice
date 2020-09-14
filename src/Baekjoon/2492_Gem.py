"""
https://www.acmicpc.net/problem/2492
Using sliding window
"""
#1. My Solution - O(T^3)
def f(x, y):
    ret = 0
    for i, j in dia:
        if x <= i <= x+k and y <= j <= y+k:
            ret += 1
    return ret


n, m, t, k = map(int, input().split())
dia = []
for i in range(t):
    dia.append([*map(int, input().split())])

ans = 0
for i in range(t):
    for j in range(t):
        xx = dia[i][0] if dia[i][0] + k < n else n - k
        yy = dia[j][1] if dia[j][1] + k < m else m - k
        temp = f(xx, yy)
        if ans < temp:
            ans = temp
            x = xx; y = yy
            
print(x, y+k)
print(ans)
