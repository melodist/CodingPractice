"""
https://www.acmicpc.net/problem/1254
Using Manacher's algorithm
"""
#1. Solution (72ms)
def palindrome(i):
    j = 0
    while i + j < n - j - 1:
        # 하나라도 성립안하면 palindrome 아님
        if s[i + j] != s[n - j - 1]:
            return False
        j += 1
    return True

s = input()
n = len(s)
 
ans = 0

# 1. 주어진 문자열의 길이 length일 때 palindrome 되는지 확인
# 2. 1번이 성립 안되면 length+1일 때 palindrome 되는지 확인
# length - 2 까지 계속 확인 ...
# length-1. length-2번이 성립 안되면 length+length-1일 때 palindrome

for i in range(n):
    if palindrome(i):
        ans = n + i
        break
    
print(ans)
