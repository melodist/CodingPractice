"""
https://programmers.co.kr/learn/courses/30/lessons/86048
나가기 전에 현재 방에 있는 인원을 계산
"""
#1. My Solution
def solution(enter, leave):
    answer = [0] * len(enter)

    for v in leave:
        now = set()
        index = 0

        for v2 in enter:
            if leave[index] not in now:  # 아직 나보다 우선순위가 앞인 숫자가 나타나지않은경우
                now.add(v2)

            while 1:
                if leave[index] in now:
                    if leave[index] == v:
                        break

                    if v not in now:  # 앞의 우선숫자가 먼저 나간경우 -> 그 숫자는 못본 것
                        now.remove(leave[index])

                    index += 1
                else:
                    break


        answer[v-1] += len(now) -1

    return answer

#2. Other Solution
def solution(enter, leave):
    answer = [0] * len(enter)

    room = set()
    e_idx = 0
    for l in leave:
        while l not in room: # l이 나가기 전에 들어온 사람을 전부 넣음
            room.append(enter[e_idx])
            e_idx += 1
        room.remove(l) # l이 나감
        for p in room: 
            answer[p - 1] += 1 # p는 l과 반드시 만남
        answer[l - 1] += len(room) # l은 room에 남아있는 사람과 반드시 만남

    return answer
