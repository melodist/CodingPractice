"""
https://programmers.co.kr/learn/courses/30/lessons/77886
Using greedy algorithm
"""
#1. My Solution
def solution(s):
    def concat(stack, cnt):
        if stack == "1" or stack == "11":
            return "110" * cnt + stack
        
        stack2 = ""
        pos = len(s) - 1
        for i, c in enumerate(stack):
            if c == "1":
                stack2 += c
                if stack2 == "111":
                    return stack[:i-2] + "110" * cnt + stack[i-2:]
            else:
                stack2 = ""
                pos = i
        
        return stack[:pos+1] + "110" * cnt + stack[pos+1:]
    
    answer = []
    for x in s:
        # '110' 제거한 문자열
        stack = ""
        cnt = 0
        for c in x:
            stack += c
            if len(stack) >= 3 and stack[-3:] == "110":
                stack = stack[:-3]
                cnt += 1

        # '110 붙이기'
        answer.append(concat(stack, cnt))

    return answer
