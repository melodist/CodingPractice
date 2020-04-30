"""
https://www.hackerrank.com/challenges/acm-icpc-team/problem
Find Maximum, Bitwise OR
"""
def acmTeam(topic):
    
    low = m = 0
    high = 1
    ans = []
    while low < len(topic) - 2:
        if high > len(topic) - 1:
            low += 1
            high = low + 1

        tmp = bin(int(topic[low], 2) | int(topic[high], 2))
        tmp_count = tmp.count('1')

        if tmp_count >= m:
            m = tmp_count
            ans.append(m)

        high += 1

    return m, ans.count(m)
