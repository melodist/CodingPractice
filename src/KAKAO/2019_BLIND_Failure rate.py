"""
https://programmers.co.kr/learn/courses/30/lessons/42889
"""
def solution(N, stages):
    clear = [0] * (N+1)
    for s in stages:
        clear[s-1] += 1

    rate = {x:0 for x in range(1, N+1)}

    for i in range(N, 0, -1):
        if clear[i-1] != 0 or clear[i] != 0:
            rate[i] = clear[i-1] / (clear[i-1] + clear[i])
            clear[i-1] += clear[i]

    return sorted(rate, key=lambda x: rate[x], reverse=True)
