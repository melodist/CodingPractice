"""
https://school.programmers.co.kr/learn/courses/30/lessons/131705
Using Combination
"""
#1. My Solution
def solution(number):
    answer = 0
    for i, a in enumerate(number):
        for j, b in enumerate(number[i+1:], i+1):
            for k, c in enumerate(number[j+1:], j+1):
                if (a+b+c) == 0:
                    answer += 1
    return answer

#2. Solution Using DFS
def solution(number):
    tot = 0
    def dfs(i, cnt, sum_num):
        nonlocal tot

        if cnt == 3 and not sum_num:
            tot += 1
            return

        if i == len(number):
            return

        if cnt < 3:
            dfs(i+1, cnt+1, sum_num + number[i])
            dfs(i+1, cnt, sum_num)

    dfs(0,0,0)        

    answer = tot


    return answer
