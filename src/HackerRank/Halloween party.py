"""
https://www.hackerrank.com/challenges/halloween-party
Mathematical Problem
"""
#1. My Solution
def halloweenParty(k):
    return (k // 2) ** 2 if k % 2 == 0 else (k // 2) * (k // 2 + 1)

#2. Other Solution
def halloweenParty(k):
    return (k // 2) * (k // 2) + (k // 2) * (k % 2)
