"""
https://school.programmers.co.kr/learn/courses/30/lessons/152996
Making counter of all weights
"""
#1. My Solution
def solution(weights):
    answer = 0
    
    count_list = [0] * 1001
    for w in weights:
        count_list[w] += 1
        
    counts = {w if c > 0 else 0:c for w,c in enumerate(count_list)}
    
    keys = set(counts.keys())
    keys_2 = set([k * 2 for k in counts.keys()])
    keys_4 = set([k * 4 for k in counts.keys()])

    for k, v in counts.items():
        if v > 1:
            answer += v * (v - 1) // 2
        
        if k * 2 in keys:
            answer += v * counts[k*2]
            
        if k * 3 in keys_2:
            answer += v * counts[(k * 3) // 2]
            
        if k * 3 in keys_4:
            answer += v * counts[(k * 3) // 4]
        
    return answer
