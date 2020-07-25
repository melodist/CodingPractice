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
        # -((p-100)//s): 배포까지 걸리는 시간 (100-p) // s는 내림한 양수가 되므로 저러한 형태의 식을 이용
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            # p, s에 해당하는 작업이 가장 뒤의 작업보다 배포까지 걸리는 시간이 짧을 경우 count를 올려줌.
            Q[-1][1]+=1
    return [q[1] for q in Q] # 최종적으로 배포까지 걸리는 시간에 해당되는 작업의 갯수를 반환.
