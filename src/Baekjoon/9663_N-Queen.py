"""
https://www.acmicpc.net/problem/9663
Backtracking Problem
"""
#1. My Solution (Timeover in python3)
class chess():
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.q = [-1] * n

    def isPossible(self, x):
        for i in range(0, x):
            if self.q[i] == self.q[x] or abs(i-x) == abs(self.q[i] - self.q[x]):
                return False
        return True

    def backtrack(self, x):
        if x == self.n-1:
            self.count += 1
            return

        for i in range(0, self.n):
            self.q[x+1] = i
            if abs(self.q[x] - i) > 1 and self.isPossible(x+1):
                self.backtrack(x+1)

    def solve(self):
        for i in range(0, self.n//2):
            self.q[0] = i
            self.backtrack(0)
        self.count *= 2
        if self.n % 2 == 0:
            return self.count
        else:
            self.q[0] = self.n//2
            self.backtrack(0)
            return self.count


queen = chess(int(input()))
print(queen.solve())

#2. Optimal Solution using bit-mask
def s(N, L, R, M):
    if M == 0: return 1
    ans = 0
    x = L&R&M
    while(x):
        lb = x&-x
        ans += s(N, ((L-lb)<<1)|1, ((R-lb)>>1)|(1<<(N-1)), M-lb)
        x -= lb
    return ans 

def s2(N, L, R, M):
    ans = 0
    for i in range((N+1)//2):
        lb = 1<<i
        v = s(N, ((L-lb)<<1)|1, ((R-lb)>>1)|(1<<(N-1)), M-lb)
        if((N&1) ==1 and i==(N-1)//2): ans += v 
        else: ans += 2*v
    return ans 

def np(N):
    return s2(N, 2**N-1, 2**N-1, 2**N-1)

print(np(int(input())))
