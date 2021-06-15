"""
https://programmers.co.kr/learn/courses/30/lessons/76502
Using Stack
"""
#1. My Solution
def solution(s):
    answer = 0
    n = len(s)
    pairs = {')':'(', ']':'[', '}':'{'}
    for i in range(n):
        s_rot = s[i:] + s[:i]
        stack = []
        flag = True
        for c in s_rot:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    flag = False
                    break
            else:
                stack.append(c)

        if flag and not stack:
            answer += 1

    return answer
