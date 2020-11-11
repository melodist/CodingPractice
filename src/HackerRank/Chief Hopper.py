"""
https://www.hackerrank.com/challenges/chief-hopper/problem
Using greedy algorithm
newEnergy = botEnergy + (botEnergy - height) >= 0
botEnergy >= height/2
"""
#1. My Solution
def chiefHopper(arr):
    e = 0
    for h in arr[::-1]:
        e = (e+h+1)//2
        
    return e
