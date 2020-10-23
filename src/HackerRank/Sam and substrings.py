"""
https://www.hackerrank.com/challenges/sam-and-substrings/problem
Using dynamic programming
"""
#1. My Solution
def substrings(n):
    MOD = 10**9 + 7
    size = len(n)
    dp = [0] * size
    dp[0] = int(n[0])
    acc = int(n[0])
    for i in range(1, size):
        dp[i] += dp[i-1] * 10 + int(n[i]) * (i+1) + acc
        acc += int(n[i]) * (i+1)
        dp[i] %= MOD

    return dp[-1]
    
#2. Other Solution
s=raw_input()
len1=len(s)
mul_ten=1
sum1=1
total_sum=len1*int(s[len1-1])
for i in range(len1-2,-1,-1):
    mul_ten = (mul_ten*10) %1000000007
    sum1 += mul_ten
    total_sum += (sum1*(i+1)) * int(s[i])) % 1000000007\
    
print total_sum%1000000007
