"""
https://programmers.co.kr/learn/courses/30/lessons/60058
Implementation Problem
"""
#1. My Solution
def seperate(p):    
    left, right = 0, 0
        
    for i, c in enumerate(p):
        if c == '(':
            left += 1
        else:
            right += 1
            
        if left == right:
            break
            
    return p[:i+1], p[i+1:]

def check(p):
    if p == '':
        return True
    
    left, right = 0, 0
        
    for c in p:
        if c == '(':
            left += 1
        else:
            right += 1
            
        if left < right:
            return False
    
    return True

def solution(p):
    if check(p):
        return p
    
    u, v = seperate(p)
    if check(u):
        return u + solution(v)
    else:
        dic = {'(':')', ')':'('}
        uu = ''
        for c in u[1:-1]:
            uu += dic[c]
        return '(' + solution(v) + ')' + uu
        
#2. Other Solution
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': 
            c-=1
        else: 
            c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i])))
