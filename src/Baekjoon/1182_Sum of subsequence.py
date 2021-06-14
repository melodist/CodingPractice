"""
https://www.acmicpc.net/problem/1182
Using backtracking
"""
#1. My Solution (624ms)
from itertools import accumulate


n, s = map(int, input().split())
a = [*map(int, input().split())]
class solve():
    def __init__(self, n, s, a):
        self.ans = 0
        self.n = n
        self.s = s
        self.a = a
        
    def backtrack(self, i, val):
        if val == self.s:
            self.ans += 1
            
        if i == self.n:
            return
        
        for j in range(i+1, self.n):
            self.backtrack(j, val+self.a[j])
            
    def loop(self):
        for i in range(n):
            self.backtrack(i, self.a[i])

solver = solve(n, s, a)
solver.loop()
print(solver.ans)

#2. Other Solution (60ms)
N,S=map(int,input().split())
T=list(map(int,input().split()))
A,B=T[:N//2],T[N//2:]
a,b=len(A),len(B)
tableA,tableB={},{}

def solution(n,sum_,i,o):
    if n==len(i):
        o[sum_]=o.get(sum_,0)+1
        return
    solution(n+1,sum_,i,o)
    solution(n+1,sum_+i[n],i,o)

solution(0,0,A,tableA)
solution(0,0,B,tableB)

tableA[0]-=1
tableB[0]-=1

ans=tableA.get(S,0)+tableB.get(S,0)
for i in tableA:
    if S-i in tableB:
        ans+=tableB[S-i]*tableA[i]
print(ans)
