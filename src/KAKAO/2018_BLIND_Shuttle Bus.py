"""
https://programmers.co.kr/learn/courses/30/lessons/17678
Input passengers in shuttle using queue.
Finally, check the last shuttle.
"""
from collections import deque, defaultdict

def convert_to_min(t):
    h, m = t.split(':')
    return int(h) * 60 + int(m)

def convert_to_hour(t):
    h = "0" + str(t // 60) if t //60 < 10 else str(t // 60)
    m = "0" + str(t % 60) if t % 60 < 10 else str(t % 60)
    return h + ":" + m

def solution(n, t, m, timetable):
    table = [convert_to_min(t) for t in timetable]
    table.sort()

    q = deque(table)

    i = 0 # Shuttle No.
    shuttle = defaultdict(list)

    while i < n and q:
        if q[0] <= i * t + 540:
            shuttle[i+1].append(q.popleft())
        else:
            i += 1

        if len(shuttle[i+1]) == m:
            i += 1

    if len(shuttle[n]) < m:
        ans = (n-1) * t + 540
    else:
        ans = shuttle[n][-1] - 1

    return convert_to_hour(ans)
