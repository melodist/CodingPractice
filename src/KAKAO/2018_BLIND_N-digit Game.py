"""
https://programmers.co.kr/learn/courses/30/lessons/17687/
Implementation Problem
"""
#1. My Solution
def digits(n, i):
    n_to_s = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    answer = ''
    while i > 0:
        q, r = divmod(i, n)
        answer += n_to_s[r]
        i = q

    return answer[::-1]


def solution(n, t, m, p):
    # n digits t answer number m people p tube turn
    # (p - 1) (p - 1 + m) (p-1 + 2*m) ... (p-1 + (t-1)*m)
    full = '0'
    i = 1
    if n != 10:
        while len(full) <= (p - 1 + (t-1) * m):
            full += digits(n, i)
            i += 1
    else:
        while len(full) <= (p - 1 + (t-1) * m):
            full += str(i)
            i += 1

    answer = [full[p-1 + i*m] for i in range(t)]
    return ''.join(answer)
    
#2. Other Solution
big = ["A","B","C","D","E","F"]
def solution(n, t, m, p):
    a="0"
    i=0
    while True:
        if len(a)>=t*m:
            break
        b=""
        j=i
        while (j):
            if j%n>9:
                b=big[j%n-10]+b
            else:
                b=str(j%n)+b
            j=j//n
        a=a+b
        i=i+1
    answer = a[p-1::m][:t]
    return answer
