"""
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/
"""
def digit_reverse(num):
    answer = 0
    while num:
        temp = num % 10
        num //= 10
        answer *= 10
        answer += temp
    return answer

def beautifulDays(i, j, k):
    answer = 0
    for x in range(i, j+1):
        if abs(x - digit_reverse(x)) % k == 0:
            answer += 1
    
    return answer
