"""
https://www.hackerrank.com/challenges/stockmax/problem
Using dynamic programming
"""
#1. My Solution
def stockmax(prices):
    prev = 0
    answer = 0
    n = len(prices)
    p_max = [0] * n
    # Store maximum value after each element
    for i, p in enumerate(prices[:0:-1], 1):
        if prev < p:
            prev = p
        p_max[n - i - 1] = prev

    for i, p in enumerate(prices[:-1]):
        if p_max[i] - p > 0:
            answer += p_max[i] - p

    return answer
