"""
https://www.hackerrank.com/challenges/sherlock-and-divisors
Mathematical Problem
"""
#1. My Solution
def divisors(n):
    answer = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 0:
                answer += 1
            if n // i != i and (n // i) % 2 == 0:
                answer += 1
            
    return answer
