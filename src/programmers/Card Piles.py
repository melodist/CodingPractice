"""
https://school.programmers.co.kr/learn/courses/30/lessons/159994
Implementation Problem
"""
#1. My Solution
def solution(cards1, cards2, goal):
    cards1 = cards1[::-1]
    cards2 = cards2[::-1]
    goal = goal[::-1]
    while cards1 and cards2 and goal:
        if cards1[-1] == goal[-1]:
            cards1.pop()
            goal.pop()
            
        if goal and cards2[-1] == goal[-1]:
            cards2.pop()
            goal.pop()
            
    return "Yes" if not goal or cards1 == goal or cards2 == goal else "No"
  
#2. Other Solution
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
