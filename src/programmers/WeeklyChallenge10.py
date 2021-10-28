"""
https://programmers.co.kr/learn/courses/30/lessons/87377

"""
#1. My Solution
def solution(line):
    
    inters = []
    for i in line:
        for j in line:
            a, b, e = i
            c, d, f = j
            
            num_x = b*f - e*d
            num_y = e*c - a*f
            den = a*d - b*c
            
            if den == 0:
                continue
            
            if (num_x % den) != 0 or (num_y % den) != 0:
                continue
            
            inters.append((num_x // den, num_y // den))

    u = -float('inf')
    d = float('inf')
    l = float('inf')
    r = -float('inf')
    
    # 격자선 구하기
    for x, y in inters:
        u = max(y, u)    
        d = min(y, d)
        l = min(x, l)
        r = max(x, r)
        
    grid = [["."] * (r - l + 1) for _ in range(u - d + 1)]

    # 격자선에 맞추기
    for x, y in inters:
        grid[u-y][x-l] = "*"
    
    return [''.join(r) for r in grid]

