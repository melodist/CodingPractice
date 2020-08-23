"""
https://programmers.co.kr/learn/courses/30/lessons/67258
Using Two Pointer Approach
"""
from collections import defaultdict


def solution(gems):
    one = defaultdict(int)
    two = set(gems)

    answer = [1, len(gems)]
    print(answer[1] - answer[0])
    start = 0
    end = 0
    while end < len(gems):
        print(one)
        if len(one) == len(two):
            if end - start < answer[1] - answer[0]:
                print(start+1, end+1)
                answer = [start+1, end+1]
                
            if one[gems[start]] == 1:
                del one[gems[start]]
            else:
                one[gems[start]] -= 1
            start += 1
        else:
            one[gems[end]] += 1
            end += 1
            

    return answer
