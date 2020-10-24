"""
https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3
Using heap
"""
#1. Solution using heap
import heapq


def solution(jobs):
    n = len(jobs)
    time, end, hq = 0, -1, []
    count = 0  # 처리한 프로세스 개수
    
    answer = 0
    while count < n:
        for start, cost in jobs:
            if end < start <= time:
                answer += (time - start)
                heapq.heappush(hq, cost)
        if len(hq) > 0:
            # 가장 빨리 끝나는 프로세스가 끝날 때까지는 hq에 있는 프로세스가 전부 대기하므로 값을 추가
            answer += len(hq) * hq[0]
            # 끝난 시간
            end = time
            # 가장 빨리 끝나는 프로세스가 걸린 시간을 더해준다
            time += heapq.heappop(hq)
            # 프로세스가 끝났으므로 count 추가
            count += 1
        else:
            # hq에 아무 것도 없으므로 시간 +1
            time += 1
            
    return answer // n
        
#2. Other Solution
def solution(jobs):
    answer = 0
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length
