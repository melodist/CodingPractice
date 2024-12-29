"""
https://www.hackerrank.com/challenges/identify-smith-numbers
Number Theory Problem
"""
#1. My Solution
def sum_digits(n):
    digits = 0
    while n != 0:
        digits += n % 10
        n = n // 10
    return digits

def sum_prime_factors(n):
    factors = 0
    factor_list = []
    while n % 2 == 0:
        factors += 2
        factor_list.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors += sum_digits(i)
            factor_list.append(i)
            n = n // i
    if n > 2:
        factor_list.append(n)
        num = sum_digits(n)
        factors += num
    return factors

def solve(n):
    factors = sum_prime_factors(n)
    digits = sum_digits(n)
    if factors == digits:
        return 1
    else:
        return 0
