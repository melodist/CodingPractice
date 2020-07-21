"""
https://programmers.co.kr/learn/courses/30/lessons/42585/
"""
#1. My Solution
def solution(arrangement):
    answer = 0
    stack = []
    arrangement = arrangement.replace('()', 'L')

    for i in arrangement:
        if i == '(':
            stack.append(0)
        elif stack and i == 'L':
            stack[-1] += 1
        elif stack:
            answer += stack.pop() * (len(stack) + 1) + 1
        
    return answer

#2. Other Solution
def solution(arrangement):
    answer = 0
    sticks = 0
    laser_to_zero = arrangement.replace('()','0')

    for i in laser_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer
