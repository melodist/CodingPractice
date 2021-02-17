"""
https://www.hackerrank.com/challenges/bon-appetit/problem
Implementation Problem
"""
#1. My Solution
def bonAppetit(bill, k, b):
    x = b - (sum(bill) - bill[k]) // 2
    print('Bon Appetit') if x == 0 else print(x)
