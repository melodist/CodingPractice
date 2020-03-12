"""
https://programmers.co.kr/learn/courses/30/lessons/42588
"""
def solution(citations):
    citations.sort()
    for i in range(len(citations), 0, -1):
        if i <= citations[len(citations) - i]:
            return i
    return 0
