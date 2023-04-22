"""
https://school.programmers.co.kr/learn/courses/30/lessons/133502
Using stack
"""
#1. My Solution
def solution(ingredient):
    stack = ""
    ans = 0
    for i in ingredient:
        stack += str(i)

        if stack[-4:] == "1231":
            stack = stack[:-4]
            ans += 1

    return ans
