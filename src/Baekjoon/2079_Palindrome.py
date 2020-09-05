"""
https://www.acmicpc.net/problem/2079
Using Dynamic Programming
How to find palindrome
1. Check edge character
2. Check inner substring is palindrome
"""
from collections import defaultdict


s = " " + input()
n = len(s)
dp = [[False] * (n+1) for _ in range(n+1)]
result = [0] * (n+1)


# Find palindrom 1 and 2 characters
for i in range(1, n+1):
	dp[i][i] = True
    
for i in range(1, n-1):
	if s[i] == s[i+1]:
		dp[i][i+1] = True
		dp[i+1][i] = True
		
# Find palindrome using dp
# i : character distance / j : start point
# j and j+1 : edge / j+1 - j+i-1 : inner substring
for i in range(2, n):
	for j in range(1, n-i):
		if s[j] == s[j + i] and dp[j + 1][j + i - 1]:
			dp[j][j + i] = dp[j + i][j] = True	
			
# Find minimum palindrome number
# result[i] : minimal palindromes exist in s[1]-s[i]
for i in range(1, n+1):
	for j in range(1, i+1):
		if dp[i][j]:
			if result[i] == 0 or result[i] > result[j - 1] + 1:
				result[i] = result[j - 1] + 1
				
print(result[n-1])
