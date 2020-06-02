"""
https://www.acmicpc.net/problem/1018
Count 2 cases.
#1. First square is B
#2. First square is W
"""
n, m = map(int, input().split())
board = [list(input().strip()) for i in range(n)]

def count(x, y):
    ans = []
    for c in ['B', 'W']:
        temp = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if ((x+y) - (i+j)) % 2 == 0:
                    if board[j][i] != c:
                        temp += 1
                else:
                    if board[j][i] == c:
                        temp += 1
        ans.append(temp)
    return min(ans)

ans = 10E10
for i in range(m-7):
    for j in range(n-7):
        temp = count(i, j)
        if ans > temp:
            ans = temp

print(ans)
