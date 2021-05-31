"""
https://programmers.co.kr/learn/courses/30/lessons/77884
"""
#1. Simple Solution
def solution(left, right):
    divisiors = [0] * 1001
    for i in range(1, 1001):
        for j in range(i, 1001):
            if j % i == 0:
                divisiors[j] += 1
                
    answer = 0
    for k in range(left, right+1):
        if divisiors[k] % 2 == 0:
            answer += k
        else:
            answer -= k
        
    return answer
    
#2. Other Solution
# 1. if i is prime -> # of divisors is 2
# 2. if i has two prime divisiors a and b -> # of divisors is 4 (1, a, b, i)
# 3. if i has three or more divisiors -> # of divisors is always even (1, i, (# of prime divisors)! )
# So i has odd divisiors when i = a^2x (x = 1, 2, ...)
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
