"""
https://programmers.co.kr/learn/courses/30/lessons/42885
"""
#1. My Solution

def solution(people, limit):
    answer = 0
    people.sort()

    left = 0
    right = len(people) - 1
    while right - left >=1:
        if people[left] + people[right] <= limit:
            left += 1
            
        right -= 1
        answer += 1
        
    return answer + 1 if left == right else answer
