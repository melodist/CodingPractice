"""
https://programmers.co.kr/learn/courses/30/lessons/12982
Implementation Problem
"""
#1. My Solution
def solution(d, budget):
    if sum(d) <= budget:
        return len(d)
    
    d.sort()
    answer = 0
    while budget >= d[answer]:
        budget -= d[answer]
        answer += 1
    return answer
