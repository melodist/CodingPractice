"""
2839번: 설탕 배달
https://www.acmicpc.net/problem/2839
그리디 알고리즘을 사용하여 문제 
"""
n = int(input())

three = 0; five = n//5; n%=5
while five >= 0:
    if n%3 == 0:
        three=n//3; n%=3; break
    five -= 1; n+= 5
print(n==0 and (five+three) or -1)
