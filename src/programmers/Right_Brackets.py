"""
https://programmers.co.kr/learn/courses/30/lessons/12929
Backtracking으로 해결.
"""
class bracket:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.brackets = ['(', ')']
        
    def isPossible(self, c, front, rear):
        if c == '(':       
            return (front+1 <= self.n and \
                    front+1 >= rear and \
                    rear <= self.n)
        else:
            return (front <= self.n and \
                    front >= rear+1 and \
                    rear+1 <= self.n)     
        
    def backtrack(self, x, front, rear):
        if x == self.n * 2:
            self.count += 1
            return
        
        for c in self.brackets:
            if c == '(':                
                if self.isPossible(c, front, rear):
                    self.backtrack(x+1, front+1, rear)
            else:
                if self.isPossible(c, front, rear):
                    self.backtrack(x+1, front, rear+1)
        
    def solve(self):
        self.backtrack(0, 0, 0)
        return self.count
            
def solution(n):
    answer = bracket(n)
    return answer.solve()
