"""
https://programmers.co.kr/learn/courses/30/lessons/86053
Using Binary Search
"""
#1. My Solution
def solution(a, b, g, s, w, t):
    def possible(time):
        G_max = 0
        S_max = 0
        G_min = 0
        S_min = 0

        for i in range(n):
            # 도시별
            # 시간 내에 운반 가능한 횟수
            cnt = (time // t[i] + 1) // 2
            g_max = min(w[i] * cnt, g[i])
            s_min = min(w[i] * cnt - g_max, s[i])
            s_max = min(w[i] * cnt, s[i])
            g_min = min(w[i] * cnt - s_max, g[i])

            # 총합
            G_max += g_max
            S_min += s_min
            S_max += s_max
            G_min += g_min

        return True if a <= G_max and b <= S_max and a + b <= G_max + S_min else False

    left = 1
    right = 1e15
    
    while left < right:
        mid = (left + right) // 2
        
        if possible(mid):
            right = mid
        else:
            left = mid + 1
        
    return right
