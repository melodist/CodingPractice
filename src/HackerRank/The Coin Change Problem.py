"""
https://www.hackerrank.com/challenges/coin-change/problem
Using Dynamic Programming and Memoization
ref. https://www.ideserve.co.in/learn/coin-change-problem-number-of-ways-to-make-change
"""
def getWays(n, c):
    c.sort() # Sort coin array
    m = len(c)
    dp = [[0] * m for _ in range(n+1)]

    def numberOfWays(amount, index):
        if index == 0:
                if amount % c[index] == 0:
                    dp[amount][index] = 1
                    return 1
                else:
                    return 0

        number, i = 0, 0
        while amount - i * c[index] >= 0:
            if dp[amount - i * c[index]][index-1] > 0:
                number += dp[amount - i * c[index]][index-1]
            else:
                number += numberOfWays(amount - i * c[index], index-1)
            
            i += 1

        dp[amount][index] = number
        return number
        
    return numberOfWays(n, m-1)
