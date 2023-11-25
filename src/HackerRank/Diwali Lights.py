"""
https://www.hackerrank.com/challenges/diwali-lights
Mathematical Problem
"""
#1. My Solution
def lights(n):
    return (2 ** n) % (10 ** 5) - 1
