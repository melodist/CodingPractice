"""
하노이의 탑
https://programmers.co.kr/learn/courses/30/lessons/12946?language=python3
재귀로 풀면 시간초과 발생. 스택을 이용한 비재귀로 해결해야 함.
"""
def solution(n):
    # start, temp, end -> start, end, temp
    start, temp, end = 1, 2, 3
    stack = []
    answer = []
    while True:
        while n > 1:
            stack.append(end)
            stack.append(temp)
            stack.append(start)
            stack.append(n)
            n -= 1
            stack.append(temp)
            temp = end
            end = stack.pop()

        answer += [[start, end]]

        # start, temp, end -> temp, start, end
        if stack:
            n = stack.pop()
            start = stack.pop()
            temp = stack.pop()
            end = stack.pop()

            answer += [[start, end]]

            n -= 1

            stack.append(start)
            start = temp
            temp = stack.pop()     
        else:
            break
    
    return answer
