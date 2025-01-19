"""
https://www.hackerrank.com/challenges/choose-and-calculate
Combinatorics Problem

1. Sort the balls in ascending order by their numbers.
2. For each ball:
  - Calculate the number of times it's selected as the maximum value.
  - Calculate the number of times it's selected as the minimum value.
  - Find the difference between these two frequencies.
3. Multiply each ball's number by the calculated difference and sum for all balls.
4. Apply modular arithmetic to the final result.
"""
#1. My Solution
def solve(balls, k):
    balls.sort()

    if k == 1:
        return 0
        
    left = 1
    right = 1
    ans = 0        

    for i in range(1, k):
        right = right * (n-i) // i
        
    for i in range(0, n):
        if i >= k-1:
            ans = ans + balls[i] * left
            left = left * (i+1) // (i-k+2)
        if i <= n-k:
            ans = ans - balls[i] * right
            right = right * (n-i-k) // (n-i-1)

    ans = ans % (10**9 + 7)

    return ans
