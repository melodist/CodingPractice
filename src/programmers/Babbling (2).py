"""
https://school.programmers.co.kr/learn/courses/30/lessons/133499
String Problem
"""
#1. My Solution
def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0

    for b in babbling:
        prev = ""
        flag = False

        while b:
            flag = False
            for w in words:
                if prev == w:
                    continue

                len_w = len(w)
                if len(b) >= len_w and b[:len_w] == w:
                    prev = w
                    b = b[len_w:]
                    flag = True
                    break

            if not flag:
                break

        if len(b) == 0:
            answer += 1

    return answer

#2. Other Solution
def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i=i.replace(j,' ')
        if len(i.strip())==0:
            answer +=1
    return answer
