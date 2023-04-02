"""
https://school.programmers.co.kr/learn/courses/30/lessons/136798
Using divisors are symmetric
"""
#1. My Solution
def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        temp = 0
        for j in range(1, int(i**0.5)+1):
            if i == j ** 2:
                temp += 1
            elif i % j == 0:
                temp += 2

            if temp > limit:
                temp = power
                break

        answer += temp

    return answer
