"""
"""
#1. My Solution
from collections import deque
import math


def solution(progresses, speeds):
    days = 0
    p = deque(progresses)
    s = deque(speeds)
    answer = []

    while p:
        jobs = 1
        now_p = p.popleft()
        now_s = s.popleft()
        days = math.ceil((100 - now_p) / now_s)
        while p and p[0] + days * s[0] >= 100:
            p.popleft()
            s.popleft()
            jobs += 1
        answer.append(jobs)

    return answer
    
#2. Other Solution
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
