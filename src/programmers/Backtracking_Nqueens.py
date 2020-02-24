"""Backtracking_Nqueens.py
어떤 노드의 유망성을 검사하고, 유망하지 않으면 부모 노드로 돌아가서 다음 자식 노드를 검사한다.
"""
class chess():
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.q = [-1] * n

    def isPossible(self, x):
        # 새로운 퀸과 같은 y좌표를 갖거나 대각선에 위치한 퀸이 있는지 검사
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
            if self.q[x] == self.q[x+1] or abs(self.q[x] - i) == 1:
                continue
            else:
                if self.isPossible(x+1):
                    self.backtrack(x+1)
                else:
                    continue

    def solve(self):
        # 체스판의 절반만 검사하고 대칭 관계를 이용하여 경우의 수를 계산
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

def solution(n):
    queen = chess(n)
    return queen.solve()
