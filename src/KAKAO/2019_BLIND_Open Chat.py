"""
https://programmers.co.kr/learn/courses/30/lessons/42888/
"""
#1. My Solution
def solution(record):
    uids = {}
    logs = []

    for string in record:
        s = string.split() 
        if s[0] == 'Enter':
            logs.append((s[0], s[1]))
            uids[s[1]] = s[2]
        elif s[0] == 'Leave':
            logs.append((s[0], s[1]))
        else:
            uids[s[1]] = s[2]

    answer = []    
    for com, uid in logs:     
        if com == 'Enter':
            answer.append(f'{uids[uid]}님이 들어왔습니다.')
        else:
            answer.append(f'{uids[uid]}님이 나갔습니다.')

    return answer
    
#2. Other Solution
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
