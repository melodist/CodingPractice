"""
https://programmers.co.kr/learn/courses/30/lessons/77885
Using bit calculation
맨 뒷자리부터 올라가면서 가장 먼저 등장하는 01 -> 10으로 바꿔야 함
ex. 0b10001111 -> 0b10010111
val ^ val+1 >> 2를 통하여 val에서 가장 먼저 등장하는 0 이전에 1로만 이루어진 부분을 분리
val ^ val+1 >> 2 = 0b111
val+1은 val에서 0 이전에 나온 1로 이루어진 부분을 전부 0으로 만들고
val ^ val+1 >> 2는 1로만 이루어진 부분의 길이에서 1만큼 짧은 1로만 이루어진 수를 반환
두 값을 더하면 답을 구할 수 있음
"""

#1. My Solution
def solution(numbers):
    answer = []
    for n in numbers:
        shift = 0
        m = n
        flag = True
        while m > 2:
            # 01 -> 10
            if bin(m)[-2:] == '01':
                answer.append((m+1)<<shift | ((1<<shift) - 1))
                flag = False
                break
            # 0 -> 1
            if m % 2 == 0:
                answer.append((m+1)<<shift | ((1<<shift) - 1))
                flag = False
                break
            shift += 1
            m = m >> 1
        if flag:
            answer.append(n+1 | n>>1)

    return answer
    
#2. Other Solution

# val^val+1 : 0b1
# (val^val+1) >> 2: 0b0
# answer 0 + 1000 + 1 -> 0b1001
def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) + (val+1))

    return answer
