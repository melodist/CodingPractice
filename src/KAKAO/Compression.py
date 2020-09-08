"""
https://programmers.co.kr/learn/courses/30/lessons/17684/
Implementation Problem
Using dictionary comprehension
"""
#1. My Solution
def solution(msg):
    alpha = [chr(ord('A') + i) for i in range(26)]
    dic = {k : v for k, v in zip(alpha, range(1, 27))}
    answer = []

    n, i = len(msg), 1
    if n == 1:
        return [dic[msg]]

    curr = msg[0]
    count = 27
    while i < n:
        curr = msg[i-1]
        while i < n and curr in dic:
            curr += msg[i]
            prev = curr[:-1]
            i += 1

        if curr not in dic:
            answer.append(dic[prev])
            dic[curr] = count
            count += 1
            if i == n:
                answer.append(dic[msg[i-1]])
        else:
            answer.append(dic[curr])

    return answer
    
#2. Other Solution
def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1  # Using this code, we can take all cases
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
