"""
https://programmers.co.kr/learn/courses/30/lessons/43163
"""
#1. My Solution
from collections import deque


def check(begin, target):
    diff = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            diff += 1
        if diff > 1:
            return False

    return True if diff == 1 else False


def solution(begin, target, words):
    visited = []
    ans = 0
    q = deque([(begin, 0)])
    while q:
        cur, n = q.popleft()
        if cur == target:
            return n
        for word in set(words) - set(visited):
            if check(cur, word):
                visited.append(word)
                q.append((word, n+1))

    return ans
    
    
#2. More Pythonic Solution using generator
from collections import deque


def check(current, words):
    for word in words:
        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1
                
        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin:0}
    q = deque([begin])
    while q:
        cur = q.popleft()

        for word in check(cur, words):
            if word not in dist:
                dist[word] = dist[cur] + 1
                q.append(word)
            
    return dist.get(target, 0)
