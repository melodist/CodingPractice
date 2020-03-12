"""
https://programmers.co.kr/learn/courses/30/lessons/42588
"""
def solution(heights):
    answer = []
    towers = len(heights)
    for i in range(towers):
        now = heights.pop()
        temp = heights.copy()
        for j in range(towers - i - 1,0,-1):
            a = temp.pop()
            if now < a:
                answer.append(j)
                break

        if len(answer) == i:
            answer.append(0)

    answer.reverse()
    return answer
