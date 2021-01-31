"""
https://programmers.co.kr/learn/courses/30/lessons/72412?language=python3
Using binary search
"""
#1. My Solution
import bisect


def solution(info, query):
    a = {'cpp':0, 'java':1, 'python':2}
    b = {'backend':0, 'frontend':1}
    c = {'junior':0, 'senior':1}
    d = {'chicken':0, 'pizza':1}
    
    table = [[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    
    for i in info:
        e, f, g, h, x = i.split()
        table[a[e]][b[f]][c[g]][d[h]].append(int(x))
    
    for a1 in range(3):
        for b1 in range(2):
            for c1 in range(2):
                for d1 in range(2):
                    table[a1][b1][c1][d1].sort()  # Sort table for binary search

    answer = []
    for q in query:
        e, _, f, _, g, _, h, x = q.split()
        x = int(x)
        temp = 0
        for a1 in range(3):
            if e != '-' and a[e] != a1:
                    continue
            for b1 in range(2):
                if f != '-' and b[f] != b1:
                    continue
                for c1 in range(2):
                    if g != '-' and c[g] != c1:
                        continue
                    for d1 in range(2):
                        if h != '-' and d[h] != d1:
                            continue
                        lower_bound = bisect.bisect_left(table[a1][b1][c1][d1], x)  # Find lower bound using binary search
                        temp += len(table[a1][b1][c1][d1]) - lower_bound
        
        answer.append(temp)
    return answer
