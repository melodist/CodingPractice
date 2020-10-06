"""
https://www.hackerrank.com/challenges/gridland-metro/problem
Merge overlapping intervals
"""
#1. My Solution
def gridlandMetro(n, m, k, track):
    if not track:
        return n * m

    track.sort()
    ans = n * m
    r0, c1, c2 = track[0]
    stack = [(r0 * n + c1, r0 * n + c2)]

    for r, c1, c2 in track[1:]:
        start = r * n + c1
        end = r * n + c2

        s_start = stack[-1][0]
        s_end = stack[-1][1]
        
        if start > s_end:
            stack.append((start, end))
        elif s_end < end:
            stack.pop()
            stack.append((s_start, end))

    while stack:
        start, end = stack.pop()
        ans -= end - start + 1

    return ans
    
#2. Other Solution
n, m, k = map(int, raw_input().split())
grid_points = 0
mapper = {}
for _ in range(k):
    r, c1, c2 = map(int, raw_input().split())
    if r in mapper:
        mapper[r].append((c1, c2))
    else:
        mapper[r] = [(c1, c2)]
for k in mapper:
    temp = mapper[k]
    temp.sort()
    begin = temp[0][0]
    end = temp[0][1]
    points = 0
    for i in range(1, len(temp)):
        if temp[i][0] > end:
            points += end - begin + 1
            begin = temp[i][0]
            end = temp[i][1]
        else:
            end = max(end, temp[i][1])
    points += end - begin + 1
    grid_points += points
print(m*n - grid_points)
