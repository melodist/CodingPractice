"""
https://programmers.co.kr/learn/courses/30/lessons/17676
1. Make Timestamps
2. Check each log is executed during timestamp ~ timestamp + 1
2-1. Starts later or ends earlier
2-2. Starts earlier and ends later
"""
def time_to_sec(string):
    _, s, t = string.split()
    end = sum([a*b for a, b in zip(map(float, s.split(':')), [3600, 60, 1])])
    return (end - float(t[:-1]) + 0.001, end)

def solution(lines):
    starts = [0] * len(lines)
    ends = [0] * len(lines)
    for i in range(len(lines)):
        starts[i], ends[i] = time_to_sec(lines[i])

    times = starts + ends
    print(times)
    ans = 0
    for start in times:
        temp = 0
        for i in range(len(lines)):
            if start <= starts[i] < start + 1 or start <= ends[i] < start + 1:
                temp += 1
            elif starts[i] <= start and ends[i] > start + 1:
                temp += 1

        ans = max(ans, temp)

    return ans
