"""
https://school.programmers.co.kr/learn/courses/30/lessons/161990
"""
#1. My Solution
def solution(wallpaper):
    lux = luy = float('inf')
    rdx = rdy = 0
    for i, row in enumerate(wallpaper):
        for j, p in enumerate(row):
            if p == '#':
                lux = min(j, lux)
                luy = min(i, luy)
                rdx = max(j, rdx)
                rdy = max(i, rdy)

    return [luy, lux, rdy+1, rdx+1]
  
#2. Other Solution
def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]
