"""
https://programmers.co.kr/learn/courses/30/lessons/67258
Using Two Pointer Approach
"""
#1. My Solution
from collections import defaultdict


def solution(gems):
    one = defaultdict(int)
    two = set(gems)

    answer = [1, len(gems)]
    start = 0
    end = 0
    
    while True:
        if len(one) == len(two):
            if end - start < answer[1] - answer[0] + 1:
                answer = [start+1, end]
                
            if one[gems[start]] == 1:
                del one[gems[start]]
            else:
                one[gems[start]] -= 1
                
            if start == len(gems):
                break
            start += 1
        else:
            if end == len(gems):
                break
            one[gems[end]] += 1
            end += 1
            
    return answer

#2. Other Solution
from collections import defaultdict


def solution(gems):
    candidates = []
    start, end = 0, 0
    gems_len, gem_kind = len(gems), len(set(gems))
    answer = [1, gems_len]
    gems_dict = defaultdict(int)
    
    while True:
        kind = len(gems_dict)
        if start == gems_len:
            break
        if kind == gem_kind:
            if end - start < answer[1] - answer[0] + 1:
                answer = [start+1, end]
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            continue
        if end == gems_len:
            break
        if kind != gem_kind:
            gems_dict[gems[end]] += 1
            end += 1
            continue

    return answer
