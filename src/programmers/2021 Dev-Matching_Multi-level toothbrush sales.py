"""
https://programmers.co.kr/learn/courses/30/lessons/77486
Implementation Problem
"""
#1. My Solution
from collections import defaultdict


def solution(enroll, referral, seller, amount):
    tree = {}
    for e, r in zip(enroll, referral):
        tree[e] = r
        
    tree['-'] = '0'
    
    perf = defaultdict(int)
    for s, a in zip(seller, amount):
        profit = a * 100
        r = tree[s]
        
        while profit >= 10 and r != '0':          
            rest = int(profit * 0.1)
            perf[s] += profit - rest

            profit //= 10        
            s = r
            r = tree[s]

        perf[s] += profit
            
    answer = []
    for e in enroll:
        answer.append(perf[e])
        
    return answer
